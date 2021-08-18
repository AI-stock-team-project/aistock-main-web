from django.shortcuts import redirect, render
from django.db.models import Max
from django.http import HttpResponseRedirect, HttpResponse
from board.models import BoardPost, BoardConfig
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from urllib.parse import urlencode
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import F


# 게시판 보기. (글 목록)
def index(request, route_id):
    """
    게시물 목록
    """
    # 게시판 설정 조회 및 유효성 체크
    board = BoardConfig.objects.filter(route=route_id).first()
    if board is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('/')

    # 페이지 변수
    page = int(request.GET.get('page', '1'))
    # 목록에서 표현되는 게시글 수 
    per_page = 8


    # 조회 쿼리
    results = BoardPost.objects.filter(board_id=board.id).order_by('-g_no', 'o_no')

    paginator = Paginator(results, per_page=per_page)
    # paginator = Paginator(results, per_page=10, orphans=5)
    main_list = paginator.get_page(page)

    currentParams = {}
    if page > 1 :
        currentParams['page'] = page

    # view rendering
    context = {
        'main_list': main_list,
        'board' : board,
        'baseurl' : reverse('board:index', kwargs={'route_id':route_id}),
        'queryStringExtend' : convQueryStringParams(currentParams),
        'queryString' : convQueryStringParams(currentParams, '?')
    }
    return render(request, 'board/index.html', context)


def convQueryStringParams(params, prefix='&'):
    if len(params) > 0:
        return prefix + urlencode(params)
    else:
        return ''


# 게시글 읽기
def view(request, route_id, post_id):
    # 게시판 설정 조회 및 유효성 체크
    board = BoardConfig.objects.filter(route=route_id).first()
    if board is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('/')

    # 게시물 번호
    # post_id = request.GET.get('id')
    if post_id is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)
        # return HttpResponse('잘못된 접근입니다.')

    post = BoardPost.objects.filter(id=post_id).first()
    if post is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)
        # return HttpResponse('없는 게시글입니다.')

    # 조회수 증가
    post.hit = post.hit + 1
    post.save()

    # 페이지 변수 (물고다니는 변수임)
    page = int(request.GET.get('page', '1'))
    currentParams = {}
    if page > 1 :
        currentParams['page'] = page

    # view rendering
    context = {
        'post': post,
        'board' : board,
        'baseurl': reverse('board:index', kwargs={'route_id':route_id}),
        'queryStringExtend' : convQueryStringParams(currentParams),
        'queryString' : convQueryStringParams(currentParams, '?'),
    }
    return render(request, "board/view.html", context)


@login_required()
def write(request, route_id):
    """
    게시판 > 글 쓰기
    """
    # 게시판 설정 조회 및 유효성 체크
    board = BoardConfig.objects.filter(route=route_id).first()
    if board is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('/')

    # 권한 체크 (로그인 해제되었거나 잘못된 접근)
    if not request.user.is_active:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)

    # 페이지 변수 (물고다니는 변수임)
    page = int(request.GET.get('page', '1'))
    currentParams = {}
    if page > 1 :
        currentParams['page'] = page
    
    # view rendering
    context = {
        'board' : board,
        'baseurl' : reverse('board:index', kwargs={'route_id':route_id}),
        'queryString' : convQueryStringParams(currentParams, '?')
    }
    return render(request, "board/writeform.html", context)


@login_required()
def post_store(request, route_id):
    """
    게시판 > 글 쓰기 > 처리
    """
    # 게시판 설정 조회 및 유효성 체크
    board = BoardConfig.objects.filter(route=route_id).first()
    if board is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('/')

    # 권한 체크 (로그인 해제되었거나 잘못된 접근)
    if not request.user.is_active:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)
        # return redirect('/board/')

    # 파라미터 조회
    title = request.POST.get('title', '')
    contents = request.POST.get('contents', '')

    # 답변글 기능을 위한 부분
    # max_gno = BoardPost.objects.aggregate(g_no=Max('g_no'))['g_no']
    # if max_gno is None or max_gno == '':
    #    max_gno = 0

    # 저장 처리
    post = BoardPost()
    post.title = title
    post.contents = contents
    post.author = request.user
    post.board = board
    # post.g_no = int(max_gno) + 1
    post.save()

    # 답변글 기능을 위한 g_no 처리
    post.g_no = post.id
    post.save()

    # 완료
    messages.info(request, '글이 새로 작성되었습니다.')
    return redirect('board:view', route_id=route_id, post_id=post.id)


@login_required()
def edit(request, route_id, post_id):
    """
    게시판 > 글 수정
    """
    # 게시판 설정 조회 및 유효성 체크
    board = BoardConfig.objects.filter(route=route_id).first()
    if board is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('/')

    # 권한 체크 (로그인 해제되었거나 잘못된 접근)
    if not request.user.is_active:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)

    # post_id 파라미터가 없음
    # post_id = request.GET.get('id')
    if post_id is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)

    # post_id 파라미터의 유효성 체크
    post = BoardPost.objects.get(id=post_id)
    if post is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)

    # view url
    view_url = reverse('board:view', kwargs={'route_id':route_id, 'post_id':post_id})
    
    # 작성자 여부 + 관리자 여부
    if not request.user.is_superuser and post.author != request.user:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect(view_url)

    # 페이지 변수 (물고다니는 변수임)
    page = int(request.GET.get('page', '1'))
    currentParams = {}
    if page > 1 :
        currentParams['page'] = page
    
    # view rendering
    context = {
        'post': post,
        'board' : board,
        'view_url' : view_url,
        'queryString' : convQueryStringParams(currentParams, '?')
    }
    return render(request, "board/updateform.html", context)


@login_required()
def update(request, route_id):
    """
    게시판 > 글 수정 > 처리
    """
    # 게시판 설정 조회 및 유효성 체크
    board = BoardConfig.objects.filter(route=route_id).first()
    if board is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('/')

    # 권한 체크 (로그인 해제되었거나 잘못된 접근)
    if not request.user.is_active:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)
    
    # post_id 파라미터가 없음
    post_id = request.POST.get('id')
    if post_id is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)

    # post_id 파라미터의 유효성 체크
    post = BoardPost.objects.get(id=post_id)
    if post is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)

    # 작성자 여부 + 관리자 여부
    if not request.user.is_superuser and post.author != request.user:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:view', route_id=route_id, post_id=post_id)

    # 파라미터 조회
    title = request.POST.get('title', '')
    contents = request.POST.get('contents', '')

    # 변경 처리
    post.title = title
    post.contents = contents
    post.save()

    # 완료
    messages.info(request, '변경이 완료되었습니다.')
    return redirect('board:view', route_id=route_id, post_id=post.id)


@login_required()
def delete(request, route_id, post_id):
    """
    게시판 > 글 삭제 처리
    """
    # 게시판 설정 조회 및 유효성 체크
    board = BoardConfig.objects.filter(route=route_id).first()
    if board is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('/')

    # 권한 체크 (로그인 해제되었거나 잘못된 접근)
    if not request.user.is_active:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)

    # post_id 파라미터가 없음
    # post_id = request.GET.get('id')
    if post_id is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)

    # post_id 파라미터의 유효성 체크
    post = BoardPost.objects.get(id=post_id)
    if post is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)

    # 작성자 여부 + 관리자 여부
    if not request.user.is_superuser and post.author != request.user:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:view', route_id=route_id, post_id=post_id)

    # 삭제 처리
    post.delete()

    # 완료
    messages.info(request, '삭제가 완료되었습니다.')
    return redirect('board:index', route_id=route_id)


@login_required()
def reply(request, route_id, post_id):
    """
    게시판 > 답변 글 작성
    """
    # 게시판 설정 조회 및 유효성 체크
    board = BoardConfig.objects.filter(route=route_id).first()
    if board is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('/')

    # 권한 체크 (로그인 해제되었거나 잘못된 접근)
    if not request.user.is_active:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)

    # post_id 파라미터가 없음
    # post_id = request.GET.get('id')
    if post_id is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)

    # post_id 파라미터의 유효성 체크
    post = BoardPost.objects.get(id=post_id)
    if post is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)

    # 페이지 변수 (물고다니는 변수임)
    page = int(request.GET.get('page', '1'))
    currentParams = {}
    if page > 1 :
        currentParams['page'] = page

    # view url
    view_url = reverse('board:view', kwargs={'route_id':route_id, 'post_id':post_id})

    # view rendering
    context = {
        'origin': post,
        'baseurl': '/board',
        'board' : board,
        'view_url' : view_url,
        'queryString' : convQueryStringParams(currentParams, '?')
    }
    return render(request, 'board/replyform.html', context)


# 답변글 처리
@login_required()
def reply_store(request, route_id, origin_post_id):
    """
    게시판 > 답변 글 작성 > 처리
    """
    # 게시판 설정 조회 및 유효성 체크
    board = BoardConfig.objects.filter(route=route_id).first()
    if board is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('/')

    # 권한 체크 (로그인 해제되었거나 잘못된 접근)
    if not request.user.is_active:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)

    # post_id 파라미터의 유효성 체크
    origin_post = BoardPost.objects.get(id=origin_post_id)
    if origin_post is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('board:index', route_id=route_id)

    # 상위의 'o_no'를 기준으로 동일한 그룹(g_no)안에서 
    # o_no가 큰 것들을 전부 +1 시켜준다. 
    # (즉, 한칸씩 밑으로 더 내린다. 그 중간에 새로운 답변글이 위치해야함)
    BoardPost.objects.filter(g_no=origin_post.g_no, o_no__gt=origin_post.o_no).update(
        o_no = F('o_no')+1
    )

    # 파라미터 조회
    title = request.POST.get('title', '')
    contents = request.POST.get('contents', '')

    # 변경 처리
    post = BoardPost()
    post.title = title
    post.contents = contents
    post.author = request.user
    post.board = board
    post.g_no = int(origin_post.g_no)
    post.o_no = int(origin_post.o_no) + 1
    post.depth = int(origin_post.depth) + 1
    post.save()

    # ret = Board.reply(data)
    # if ret != 1:
    #    return HttpResponse('오류 발생')
    return redirect('board:view', route_id=route_id, post_id=post.id)
    # return redirect('/board/')

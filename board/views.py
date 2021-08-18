from django.shortcuts import redirect, render
from django.db.models import Max
from django.http import HttpResponseRedirect, HttpResponse
from board.models import Board, BoardConfig
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from urllib.parse import urlencode
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse


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
    results = Board.objects.filter(board_id=board.id).order_by('-g_no', 'o_no')

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

    post = Board.objects.filter(id=post_id).first()
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
        return redirect('/board/')

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
        return redirect('/board/')

    title = request.POST.get('title', '')
    contents = request.POST.get('contents', '')

    # 답변글 기능을 위한 부분
    max_gno = Board.objects.aggregate(g_no=Max('g_no'))['g_no']
    if max_gno is None or max_gno == '':
        max_gno = 0

    # 저장 처리
    post = Board()
    post.title = title
    post.contents = contents
    post.author = request.user
    post.g_no = int(max_gno) + 1
    post.save()

    # board = Board(title=title, contents=contents, user=user)
    # board.save()

    # ret = Board.insert(data)
    # if ret != 1:
    #     return HttpResponse('오류 발생')

    return redirect(f'/board/view/?id={post.id}')


@login_required()
def edit(request, route_id):
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
        return redirect('/board/')

    # post_id 파라미터가 없음
    post_id = request.GET.get('id')
    if post_id is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('/board/')

    # post_id 파라미터의 유효성 체크
    post = Board.objects.get(id=post_id)
    if post is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('/board/')

    # 작성자 여부 + 관리자 여부
    if not request.user.is_superuser and post.author != request.user:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect(f'/board/view/?id={post_id}')

    context = {
        'post': post,
        'baseurl': '/board'
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
        return redirect('/board/')
    
    # post_id 파라미터가 없음
    post_id = request.POST.get('id')
    if post_id is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('/board/')

    # post_id 파라미터의 유효성 체크
    post = Board.objects.get(id=post_id)
    if post is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('/board/')

    # 작성자 여부 + 관리자 여부
    if not request.user.is_superuser and post.author != request.user:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect(f'/board/view/?id={post_id}')

    title = request.POST.get('title', '')
    contents = request.POST.get('contents', '')

    # 변경 처리
    post.title = title
    post.contents = contents
    post.save()

    return redirect(f'/board/view/?id={post.id}')


@login_required()
def delete(request, route_id):
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
        return redirect('/board/')

    # post_id 파라미터가 없음
    post_id = request.GET.get('id')
    if post_id is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('/board/')

    # post_id 파라미터의 유효성 체크
    post = Board.objects.get(id=post_id)
    if post is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('/board/')

    # 작성자 여부 + 관리자 여부
    if not request.user.is_superuser and post.author != request.user:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect(f'/board/view/?id={post_id}')

    # 삭제 처리
    post.delete()

    return redirect(f'/board/')


@login_required()
def reply(request, route_id):
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
        return redirect('/board/')

    # post_id 파라미터가 없음
    post_id = request.GET.get('id')
    if post_id is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('/board/')

    # post_id 파라미터의 유효성 체크
    post = Board.objects.get(id=post_id)
    if post is None:
        messages.error(request, '권한이 없거나 경로가 잘못되었습니다.')
        return redirect('/board/')

    context = {
        'origin': post,
        'baseurl': '/board'
    }
    return render(request, 'board/replyform.html', context)


# 답변글 처리
@login_required()
def reply_store(request, route_id):
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
        return redirect('/board/')

    title = request.POST.get('title', '')
    contents = request.POST.get('contents', '')

    g_no = request.POST.get('g_no', 0)
    o_no = request.POST.get('o_no', 0)
    depth = request.POST.get('depth', 0)

    # 변경 처리
    board = Board()
    board.title = title
    board.contents = contents
    board.author = request.user
    board.g_no = int(g_no)
    board.o_no = int(o_no) + 1
    board.depth = int(depth) + 1
    board.save()

    # ret = Board.reply(data)
    # if ret != 1:
    #    return HttpResponse('오류 발생')

    return redirect('/board/')

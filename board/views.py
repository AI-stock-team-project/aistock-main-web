from django.shortcuts import render
from django.db.models import Max
from django.http import HttpResponseRedirect, HttpResponse
from math import ceil
from board.models import Board
from django.core.paginator import Paginator
from django.contrib.auth.models import User



# 게시판 보기. (글 목록)
def index(request):
    """
    게시판 보기
    """
    page = int(request.GET.get('p', '1'))

    if 'kwd' in request.GET:
        kwd = request.GET.get('kwd', '')
        # print("키워드 있음")
    else:
        kwd = ''

    LIST_COUNT = 10

    # 시작 번호
    # noinspection PyShadowingNames
    index = (page - 1) * LIST_COUNT
    results = Board.objects.all().order_by('-g_no', 'o_no')[index: index+LIST_COUNT]
    # print(results.query)

    #paginator = Paginator(results, per_page=10, orphans=5)
    #boards = paginator.page(int(page))

    totalcount = Board.objects.count()
    pagecount = ceil(totalcount/LIST_COUNT)
    curpage = page
    nextpage = curpage + 1 if curpage < pagecount else curpage
    prevpage = 1 if (curpage - 1) < 1 else curpage - 1

    paginator = {
        'totalcount': totalcount,
        'listcount': LIST_COUNT,
        'pagecount': pagecount,
        'nextpage': nextpage,
        'prevpage': prevpage,
        'curpage': curpage,
        'paging': range(1, 6)
    }

    # 글 시작 번호
    startcount = totalcount - (curpage - 1) * LIST_COUNT
    #print(startcount)

    data = {
        'startcount': startcount,
        'list': results,
        'keyword': kwd,
        'baseurl': '/board',
        'paginator': paginator
    }
    return render(request, 'board/index.html', data)


# 게시글 읽기
def view(request):
    postid = request.GET.get('id')
    if postid is None:
        return HttpResponse('잘못된 접근입니다.')

    # result = Board.find(postid)
    board = Board.objects.get(id=postid)

    if board is None:
        return HttpResponse('없는 게시글입니다.')

    data = {
        'post': board,
        'baseurl': '/board'
    }

    # 조회수 증가
    # Board.increment_hit(postid)
    board.hit = board.hit + 1
    board.save()

    return render(request, "board/view.html", data)


# 글 쓰기
def writeform(request):
    authuser = request.session.get('authuser')
    if authuser is None:
        # 유저가 아닌 접근이므로. 비정상 접근이거나 세션 해제된 상태.
        return HttpResponseRedirect('/')

    data = {
        'baseurl': '/board'
    }
    return render(request, "board/writeform.html", data)


# 저장 처리
def write(request):
    authuser = request.session.get('authuser')
    if authuser is None:
        # 유저가 아닌 접근이므로. 비정상 접근이거나 세션 해제된 상태.
        return HttpResponseRedirect('/')

    title = request.POST.get('title', '')
    contents = request.POST.get('contents', '')

    user = User.objects.get(id=authuser['id'])

    max_gno = Board.objects.aggregate(g_no=Max('g_no'))['g_no']
    if max_gno is None or max_gno == '':
        max_gno = 0

    # 저장 처리
    board = Board()
    board.title = title
    board.contents = contents
    board.user = user
    board.g_no = int(max_gno) + 1
    board.save()

    # board = Board(title=title, contents=contents, user=user)
    # board.save()

    # ret = Board.insert(data)
    # if ret != 1:
    #     return HttpResponse('오류 발생')

    return HttpResponseRedirect('/board/')
    # return HttpResponseRedirect('/board/view/?no=')


# 글 수정
def updateform(request):
    authuser = request.session.get('authuser')
    if authuser is None:
        # 유저가 아닌 접근이므로. 비정상 접근이거나 세션 해제된 상태.
        return HttpResponseRedirect('/')

    postid = request.GET.get('id')
    if postid is None:
        return HttpResponse('잘못된 접근입니다.')

    # result = Board.find(postid)
    board = Board.objects.get(id=postid)
    if board is None:
        return HttpResponse('없는 게시글입니다.')

    if board.user_id != authuser['id']:
        return HttpResponse('권한이 없습니다.')

    data = {
        'post': board,
        'baseurl': '/board'
    }
    return render(request, "board/updateform.html", data)


# 변경 처리
def update(request):
    authuser = request.session.get('authuser')
    if authuser is None:
        # 유저가 아닌 접근이므로. 비정상 접근이거나 세션 해제된 상태.
        return HttpResponseRedirect('/')

    postid = request.POST.get('id')
    if postid is None:
        return HttpResponse('잘못된 접근입니다.')

    # result = Board.find(postid)
    board = Board.objects.get(id=postid)
    if board is None:
        return HttpResponse('없는 게시글입니다.')

    if board.user_id != authuser['id']:
        return HttpResponse('권한이 없습니다.')

    title = request.POST.get('title', '')
    contents = request.POST.get('contents', '')

    board.title = title
    board.contents = contents
    board.save()

    return HttpResponseRedirect('/board/')


# 글 삭제 처리
def delete(request):
    authuser = request.session.get('authuser')
    if authuser is None:
        # 유저가 아닌 접근이므로. 비정상 접근이거나 세션 해제된 상태.
        return HttpResponseRedirect('/')

    postid = request.GET.get('id')
    if postid is None:
        return HttpResponse('잘못된 접근입니다.')

    # result = Board.find(postid)
    board = Board.objects.get(id=postid)
    if board is None:
        return HttpResponse('없는 게시글입니다.')

    if board.user_id != authuser['id']:
        return HttpResponse('권한이 없습니다.')

    board.delete()

    return HttpResponseRedirect('/board/')


def replyform(request):
    authuser = request.session.get('authuser')
    if authuser is None:
        # 유저가 아닌 접근이므로. 비정상 접근이거나 세션 해제된 상태.
        return HttpResponseRedirect('/')

    postid = request.GET.get('id')
    if postid is None:
        return HttpResponse('잘못된 접근입니다.')

    # result = Board.find(postid)
    board = Board.objects.get(id=postid)
    if board is None:
        return HttpResponse('없는 게시글입니다.')

    data = {
        'origin': board,
        'baseurl': '/board'
    }
    return render(request, 'board/replyform.html', data)


# 답변글 처리
def reply(request):
    authuser = request.session.get('authuser')
    if authuser is None:
        # 유저가 아닌 접근이므로. 비정상 접근이거나 세션 해제된 상태.
        return HttpResponseRedirect('/')

    title = request.POST.get('title', '')
    contents = request.POST.get('contents', '')

    g_no = request.POST.get('g_no', 0)
    o_no = request.POST.get('o_no', 0)
    depth = request.POST.get('depth', 0)

    user = User.objects.get(id=authuser['id'])

    # 저장 처리
    board = Board()
    board.title = title
    board.contents = contents
    board.user = user
    board.g_no = int(g_no)
    board.o_no = int(o_no) + 1
    board.depth = int(depth) + 1
    board.save()

    # ret = Board.reply(data)
    # if ret != 1:
    #    return HttpResponse('오류 발생')

    return HttpResponseRedirect('/board/')

#coding=utf-8

def get_session(request):
    uname = request.session.get('uname','')
    # 获取session_id
    # session_id = request.session.session_key
    return {'uname':uname}
from django.http import JsonResponse
import json
from apisuccess.Api import ChatBot as bot
from time import gmtime, strftime

def index(request):
    if request.method == 'POST':

        jsonData = json.loads(request.body.decode('utf-8'))

        msg = jsonData["msg"]
        res1 = bot.ChatBot.getBot().response(msg)

        # Limit text in paragraph
        res = res1
        for i, letter in enumerate(res):
            if i % 20 == 0:
                res += '\n'

        time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        return JsonResponse({
            "desc": "Success",
            "ques": msg,
            "res": res,
            "time": time
        })
    else:
        return JsonResponse({"desc": "Bad request"}, status=400)

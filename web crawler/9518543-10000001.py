import datetime
import requests
from bs4 import BeautifulSoup
import numpy as np
import csv
from random import randint
import threading
import time

start_number = 9518543
end_number = 10000001

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
random_agent = USER_AGENTS[randint(0, len(USER_AGENTS) - 1)]
headers = {
    'User-Agent': random_agent,
}
session = requests.Session()

now_time = datetime.datetime.now().strftime('%Y-%m-%d')

homepage_title = ["id","??????","??????","????????????","??????","??????","????????????","??????????????????", "?????????", "?????????", "?????????", "??????????????????", "????????????", "?????????","????????????","???????????????","??????????????????","?????????????????????","?????????????????????","????????????","????????????????????????", "?????????????????????(%)", "?????????????????????(%)", "???????????????????????????", "???????????????", "????????????/????????????", "????????????????????????","?????????????????????", "?????????????????????(%)", "????????????????????????", "???90?????????????????????", "???????????????", "?????????/?????????","??????????????????","??????????????????","??????????????????"]
online_wenzhen_title = ["id", "??????", "??????????????????", "????????????????????????", "??????????????????", "??????????????????","??????????????????"]

file_homepage = "/Users/qiuchutong/Desktop/all_????????????" + str(now_time) + "?????????"+str(end_number)+ ".csv"
f1 = open(file_homepage, 'a+')
f11 = csv.writer(f1)
f11.writerow(homepage_title)

file_online_wenzhen = "/Users/qiuchutong/Desktop/all_????????????" + str(now_time) + "?????????"+ str(end_number) + ".csv"
f7 = open(file_online_wenzhen, 'a+')
f77 = csv.writer(f7)
f77.writerow(online_wenzhen_title)


for doctor_id_url in range(start_number,end_number):
    homepage = []
    online_wenzhen = []
    doctor_id = doctor_id_url
    doctor_url = 'https://www.haodf.com/doctor/' + str(doctor_id) + '.html'
    print(doctor_url)
    req = session.get(doctor_url, headers=headers)
    bs = BeautifulSoup(req.text, "html.parser")
    if not bs.find_all("div", class_="profile-txt"):
        continue
    elif bs.find_all("div", class_="profile-txt"):
        # ??????????????????
        # ?????????
        visit = bs.find("span", class_="per-sta-data js-total-new-pv")
        if not (visit):
                continue
        elif visit:
            # ??????ID
            for il in bs.find_all("div", class_="profile-avatar-wrap"):
                id_find = il.find("div", class_="profile-avatar js-space")
                id_get = id_find['data-did']
            homepage.append(id_get)
            online_wenzhen.append(id_get)
            for pl in bs.find_all("div", class_="profile-txt"):
                # ????????????
                sub_name = pl.find("h1", class_="doctor-name js-doctor-name")
                homepage.append(sub_name.string)
                online_wenzhen.append(sub_name.string)
                # ?????????????????????
                for dl in pl.find_all("div", class_="doctor-titlewrap"):
                    title = pl.find("span", class_="doctor-title")
                    educate = pl.find("span", class_="doctor-educate-title")
                    if title:
                        homepage.append(title.string)
                    if educate:
                        homepage.append(educate.string)
                    elif not (title):
                        homepage.append("None")
                    elif not (educate):
                        homepage.append("None")
                hospital = []
                keshi = []
                # ???????????????
                for ul in pl.find_all("ul", class_="doctor-faculty-wrap"):
                    for li in ul.find_all("li", class_="doctor-faculty"):
                        mid = []
                        for a in li.find_all("a"):
                            mid.append(a.string)
                        if mid[0] not in hospital:
                            hospital.append(mid[0])
                        if mid[1] not in keshi:
                            keshi.append(mid[1])
            hospital = " ".join(hospital)
            keshi = " ".join(keshi)
            homepage.append(hospital)
            homepage.append(keshi)
            # ?????????????????????
            if bs.find_all("div", class_="honor-wrap"):
                for hl in bs.find_all("div", class_="honor-wrap"):
                    nd = ""
                    for ht in hl.find_all("li", class_="honor-title"):
                        jn = ht.string
                        nd = " ".join([nd, jn])
            else:
                nd = "None"
            homepage.append(nd)
            li2 = bs.find("li", class_="stat-item clearfix")
            if li2:
                ch = li2.find("span", class_="value")
                if ch:
                    homepage.append(ch.string)
            else:
                homepage.append("None")
            visit = visit.string.strip()
            visit_filter = filter(str.isdigit, visit)
            visit = "".join(visit_filter)
            homepage.append(visit)
            # ?????????
            paper = bs.find("span", class_="per-sta-data js-articleCount")
            paper = paper.string.strip()
            paper_filter = filter(str.isdigit, paper)
            paper = "".join(paper_filter)
            homepage.append(paper)
            # ?????????
            patient = bs.find("span", class_="per-sta-data js-spaceRepliedCount")
            patient = patient.string.strip()
            patient_filter = filter(str.isdigit, patient)
            patient = "".join(patient_filter)
            homepage.append(patient)
            # ??????????????????
            after_patient = bs.find("span", class_="per-sta-data js-totaldiagnosis-report")
            after_patient = after_patient.string.strip()
            after_patient_filter = filter(str.isdigit, after_patient)
            after_patient = "".join(after_patient_filter)
            homepage.append(after_patient)
            # ????????????
            comment = bs.find("span", class_="per-sta-data js-doctorVoteCnt")
            comment = comment.string.strip()
            comment_filter = filter(str.isdigit, comment)
            comment = "".join(comment_filter)
            homepage.append(comment)
            # ?????????
            thanks = bs.find("span", class_="per-sta-data js-thankLetterCount")
            thanks = thanks.string.strip()
            thanks_filter = filter(str.isdigit, thanks)
            thanks = "".join(thanks_filter)
            homepage.append(thanks)
            # ????????????
            gifts = bs.find("span", class_="per-sta-data js-presentCnt")
            gifts = gifts.string.strip()
            gifts_filter = filter(str.isdigit, gifts)
            gifts = "".join(gifts_filter)
            homepage.append(gifts)
        s_number = 0
        # ????????????
        if bs.find_all("li", class_="experience-row clearfix"):
            # ???????????????
            for el in bs.find_all("li", class_="experience-row clearfix"):
                for sl in el.find_all("img"):
                    if sl["alt"] == "????????????":
                        s_number += 1
                    else:
                        continue
            homepage.append(s_number)
            # ?????????????????????
            # ?????????????????????
            for el in bs.find_all("li", class_="experience-row clearfix"):
                if not (el.find_all("img")):
                    for ll in el.find_all("span", class_="experience-data"):
                        rl = ll.string.strip()
                        rl_filter = filter(str.isdigit, rl)
                        rl = "".join(rl_filter)
                        homepage.append(rl)
        else:
            for i in range(0, 3):
                homepage.append("None")

        # ????????????
        if bs.find_all("div", class_="js-visit-content-wrap"):
            for mz in bs.find_all("div", class_="js-visit-content-wrap"):
                place = bs.find("li", class_="faculty-item active").string
                homepage.append(place)
                sub_detail = []
                if bs.find_all("p", class_="schedule-type"):
                    for tp in bs.find_all("p", class_="schedule-type"):
                        if tp.string not in sub_detail:
                            sub_detail.append(tp.string)
                    alltim = " ".join(sub_detail)
                    homepage.append(alltim)
                else:
                    homepage.append("None")
        else:
            homepage.append("None")
            homepage.append("None")

        # ??????
        # ??????url(????????????????????????????????????url??????????????????????????????)
        if not bs.find("li", class_="g-d-w-item js-bingcheng-tab"):
            online_wenzhen.append("??????????????????????????????")
        elif bs.find("li", class_="g-d-w-item js-bingcheng-tab"):
            wz = bs.find("li", class_="g-d-w-item js-bingcheng-tab")
            wenzheng = wz.find("a", class_="g-d-w-text")
            wenzhen_url = wenzheng["href"]
            wenzhen_req = session.get(wenzhen_url, headers=headers, allow_redirects=False)
            wenzhen_bs = BeautifulSoup(wenzhen_req.text, "html.parser")

            # ????????????
            if wenzhen_bs.find("a", class_="advise_button pl10 w_b1"):
                online_wenzhen_url = wenzhen_bs.find("a", class_="advise_button pl10 w_b1")["href"]
                if "https:" not in online_wenzhen_url:
                    online_wenzhen_url = "https:" + online_wenzhen_url
                online_wenzhen_req = session.get(online_wenzhen_url, headers=headers, allow_redirects=False)
                online_wenzhen_bs = BeautifulSoup(online_wenzhen_req.text, "html.parser")
                fangshi = online_wenzhen_bs.find("div", class_="service-box")
                for shichang in fangshi.find_all("p", class_="f18 mt35b11"):
                    for shichangr in fangshi.find_all("span", class_="score_fen"):
                        shichangrate = shichangr.string
                        online_wenzhen.append(shichangrate)
                for jiage in fangshi.find_all("span", class_="service-name-price"):
                    online_wenzhen.append(jiage.string)
            else:
                online_wenzhen.append("??????????????????????????????")


        # ??????????????????
        # ????????????url(???????????????url????????????url??????????????????????????????????????????????????????????????????????????????)
        if not bs.find("li", class_="g-d-w-item js-zhenliao-tab"):
            for ofw in range(0,13):
                homepage.append("None")
        elif bs.find("li", class_="g-d-w-item js-zhenliao-tab"):
            ofl = bs.find("li", class_="g-d-w-item js-zhenliao-tab")
            ofll = ofl.find("a", class_="g-d-w-text")
            offline_url = ofll["href"]
            offline_req = session.get(offline_url, headers=headers, allow_redirects=False)
            offline_bs = BeautifulSoup(offline_req.text, "html.parser")
            # ????????????
            # ??????????????????????????????????????????????????????
            ac = offline_bs.find("div", class_="block-item vote-rate")
            for acl in ac.find_all("span", class_="sta-num"):
                acl_value = acl.contents[0].strip()
                if acl_value != "??????":
                    homepage.append(acl.contents[0].strip())
                elif acl_value == "??????":
                    homepage.append("None")
            if offline_bs.find("span", class_="vote-total-num"):
                comment_2_number = offline_bs.find("span", class_="vote-total-num").string
                homepage.append(comment_2_number)
                comment_classify_count = offline_bs.find("div", class_="filter-cate-wrap")
                for fenlei in comment_classify_count.find_all("a", class_="filter-item"):
                    if "????????????" in fenlei.string.strip():
                        continue
                    elif "????????????" in fenlei.string.strip():
                        continue
                    else:
                        fenlei_number = fenlei.string.strip()
                        fenlei_split = fenlei_number.split("(")
                        fenlei_result = fenlei_split[1].replace(")", "")
                        homepage.append(fenlei_result)
            else:
                for t in range(0, 4):
                    homepage.append("None")

            # ??????????????????
            if offline_bs.find("a", class_="c-t-right"):
                find_online = offline_bs.find("div", class_="inner-container clearfix")
                find_then = find_online.find("a", class_="c-t-right")
                online_url = find_then["href"]
                online_req = session.get(online_url, headers=headers, allow_redirects=False)
                online_bs = BeautifulSoup(online_req.text, "html.parser")
                online_number = online_bs.find("div", class_="container announce-container")
                # "?????????????????????","?????????????????????(%)","??????????????????"
                for on in online_number.find_all("span", class_="sta-num"):
                    if on.string.strip() == "??????":
                        homepage.append("None")
                    elif "%" in on.string.strip():
                        no_signal = on.string.strip().replace("%", "")
                        homepage.append(no_signal)
                    else:
                        homepage.append(on.string.strip())
                # ???90?????????????????????
                if online_bs.find("span", class_="total-txt"):
                    online_comment_number = online_bs.find("span", class_="total-txt")
                    on_num = online_comment_number.find("span", class_="num")
                    homepage.append(on_num.string)
                    # ?????????????????????
                    for gb in online_bs.find_all("a", class_="headerTag"):
                        if "??????" in gb.string.strip():
                            continue
                        else:
                            douyou = gb.string.strip()
                            douyou_split = douyou.split("(")
                            meikuohao = douyou_split[1].replace(")", "")
                            homepage.append(meikuohao)
                else:
                    for k in range(0, 3):
                        homepage.append("None")

            else:
                homepage.append("None")

        # ?????????
        # ?????????url
        # ????????????
        if bs.find("li", class_="g-d-w-item js-jiankang-tab"):
            jk = bs.find("li", class_="g-d-w-item js-jiankang-tab")
            jiankang = jk.find("a", class_="g-d-w-text")
            jiankang_url = jiankang["href"]
            jiankang_req = session.get(jiankang_url, headers=headers, allow_redirects=False)
            jiankang_bs = BeautifulSoup(jiankang_req.text, "html.parser")
            for al in jiankang_bs.find_all("div", class_="lb-tab-item"):
                find_al = al.contents[0].string.strip()
                if find_al == "??????":
                    article_number = al.contents[1].string.strip()
                    article_number_filter = filter(str.isdigit, article_number)
                    article_number = "".join(article_number_filter)
            homepage.append(article_number)
            # ?????????????????????
            for fl in jiankang_bs.find_all("div", class_="number"):
                if fl.contents[1].string.strip() == "??????":
                    fan_number = fl.contents[0].string.strip()
                    if "???" in fan_number:
                        fan_number_split = fan_number.split("???")
                        fan_number = float(fan_number_split[0])
                        fan_number = str(fan_number * 10000)
                    homepage.append(fan_number)
                elif fl.contents[1].string.strip() == "??????":
                    read_number = fl.contents[0].string.strip()
                    if "???" in read_number:
                        read_number_split = read_number.split("???")
                        read_number = float(read_number_split[0])
                        read_number = str(read_number * 10000)
                    homepage.append(read_number)
        else:
            for hn in range(0,3):
                homepage.append("None")


    print("????????????")
    print(homepage_title)
    print(homepage)
    print("??????????????????")
    print(online_wenzhen_title)
    print(online_wenzhen)


    f11.writerow(np.array(homepage))
    f77.writerow(np.array(online_wenzhen))


f1.close()
f7.close()



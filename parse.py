# -*- coding: utf-8 -*-
import urllib.request as urlre
import requests
import datetime
# If You Needs
# import urllib.parse as urlps
# from bs4 import BeautifulSoup as bs
import re as regex

opener = urlre.build_opener()

# Temporary Cookie
# TODO : Get Cookie From Site
session = "JSESSIONID=Dcqg5I1Bl9eHZCfwPXZLctaPBaMPbLQo9mbSWrAxHvjtROW19xTO0EXaIiMV3xQg.UHdlYnN2ci9zZXJ2ZXIxMw=="

# TODO : Receive By Input
day = datetime.date(2015, 12, 11)

jheaders = {
    "Accept":"text/plain, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4",
    "Connection":"keep-alive",
    "Content-Length":"149",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie":session,
    "Host":"hubbi.its.ulsan.kr",
    "Origin":"http://hubbi.its.ulsan.kr",
    "Referer":"http://hubbi.its.ulsan.kr/ingecep/launcher/embed_1.jsp?lang=ko_KR&mts=INGECEP&objid=84466814-713e496d&_d=ulsanhub",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
}
qheaders = {
    "Accept":"text/plain, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4",
    "Connection":"keep-alive",
    "Content-Length":"22539",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie":session,
    "Host":"hubbi.its.ulsan.kr",
    "Origin":"http://hubbi.its.ulsan.kr",
    "Referer":"http://hubbi.its.ulsan.kr/ingecep/launcher/embed_1.jsp?lang=ko_KR&mts=INGECEP&objid=84466814-713e496d&_d=ulsanhub",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
}
jdata = {
    "ack":"18",
    "mbody":"<smsg></smsg>",
    "option":"getjobid",
    "djobid":"",
    "theme_id":"",
    "_mts_":"0122483f-0155fb46",
    "__i":"option;djobid;theme_id",
    "uniquekey":"2017630173150",
}

while(True):
    tmrow = day + datetime.timedelta(days=1)
    r=requests.post("http://hubbi.its.ulsan.kr/ingecep/servlet/krcp", data=jdata, allow_redirects=True, headers=jheaders)
    jobid = regex.findall("<smsg><item uid='(.*)'/>", str(r.content))[0]

    qdata = {
        "ack":"18",
        "mbody":"<smsg><item uid='84466814-713e496d' name='32010_가로별 교통량(15분)' nodepath='/HUB/02_Reports/10. 통합플랫폼/32000_(상시)교통량 및 속도/32010_가로별 교통량(15분)' type='Report'><objinfo cube='a517fce3-241e413b' reportmode='rolap' version='1.1'/><Pivot b_sc_load='F' ploader='T'><Sheet  drillreport='F' isdistinct='F' fetchall='F' fw='F' fh='F' hidetitle='F' openload='F' columnfill='T' enablepivot='T' enablecache='F' tb_vch='F' tb_prt_grd='F' tb_prt='T' showlnum='F' bcluster='F' edrill='F' name='단위 : 대' viewmode='grid' objtype='SHEET' drilltarget='sheet_1^F^^' viewchange='T' toolbutton='F' tb_prt_i='excel;csv'><Pivot  measurelocation='column' customfix='F' usepaging='F' pagestyle='normal' dataquerymode='M_PIVOT' measuretitle='F' measureposition='0' customfixcols='0' rowperpage='20' isdistinct='F' fetchall='F' showlnum='F'><RowDimensions><item uid='d3a2fec6-6a36417a' name='가로명' itemtype='Metric' type='Metric' nodepath='/HUB/01_Data/10. 통합플랫폼/10. MART 모델, 큐브/큐브_ITS/구간 일반현황/가로명' memo='' sortorder='' activeformula='' aggrfunc='' disp_title='' hidecolumn='' timeformat=''/><item uid='6e4ff24c-01da4c90' name='방면' itemtype='Metric' type='Metric' nodepath='/HUB/01_Data/10. 통합플랫폼/10. MART 모델, 큐브/큐브_ITS/구간 일반현황/방면' memo='' sortorder='' activeformula='' aggrfunc='' disp_title='' hidecolumn='T' timeformat=''/><item uid='5e9cc154-4f984963' name='순번(LV2)' itemtype='Metric' type='Metric' nodepath='/HUB/01_Data/10. 통합플랫폼/10. MART 모델, 큐브/큐브_ITS/속도, 교통량/순번(LV2)' memo='' sortorder='' activeformula='' aggrfunc='' disp_title='' hidecolumn='T' timeformat=''/><item uid='6cef7afb-926249c2' name='시작지점' itemtype='Metric' type='Metric' nodepath='/HUB/01_Data/10. 통합플랫폼/10. MART 모델, 큐브/큐브_ITS/속도, 교통량/시작지점' memo='' sortorder='' activeformula='' aggrfunc='' disp_title='' hidecolumn='' timeformat=''/><item uid='83c0f68a-936d4207' name='종료지점' itemtype='Metric' type='Metric' nodepath='/HUB/01_Data/10. 통합플랫폼/10. MART 모델, 큐브/큐브_ITS/속도, 교통량/종료지점' memo='' sortorder='' activeformula='' aggrfunc='' disp_title='' hidecolumn='' timeformat=''/><item uid='cfcd1354-94414cb4' name='기준분' itemtype='Metric' type='Metric' nodepath='/HUB/01_Data/10. 통합플랫폼/10. MART 모델, 큐브/큐브_ITS/속도, 교통량/기준분' memo='' sortorder='' activeformula='' aggrfunc='' disp_title='분' hidecolumn='F' timeformat=''/></RowDimensions><ColumnDimensions><item uid='baa7defe-3ceb421e' name='기준시간' itemtype='Metric' type='Metric' nodepath='/HUB/01_Data/10. 통합플랫폼/10. MART 모델, 큐브/큐브_ITS/속도, 교통량/기준시간' memo='' sortorder='' activeformula='' aggrfunc='' disp_title='시간' hidecolumn='F' timeformat=''/></ColumnDimensions><Measures><item uid='37499a1f-997a400d' name='교통량(15분)_평균' itemtype='Measure' type='Measure' nodepath='/HUB/01_Data/10. 통합플랫폼/10. MART 모델, 큐브/큐브_ITS/measures/교통량(15분)_평균' memo='' sortorder='' activeformula='' aggrfunc='' disp_title='승용차' hidecolumn='F' timeformat=''/><item uid='38a69d15-639f4d20' name='버스 교통량(15분)_평균' itemtype='Measure' type='Measure' nodepath='/HUB/01_Data/10. 통합플랫폼/10. MART 모델, 큐브/큐브_ITS/measures/버스 교통량(15분)_평균' memo='' sortorder='' activeformula='' aggrfunc='' disp_title='버스' hidecolumn='F' timeformat=''/></Measures><QueryItems></QueryItems><Clusters></Clusters><rptitems><rptitem name='단위 피봇 설계'><Filter></Filter><HavingFilter></HavingFilter></rptitem></rptitems></Pivot><UserDefinedGroup/><sql_prompts></sql_prompts><Filter></Filter><HavingFilter></HavingFilter><AuxFilter><FilterData><Filter><Row uid='b582538f-204c4af6' name='기준일자(15분)' type='Metric' operator='BETWEEN' title='기준일자' useprompt='F'><code><![CDATA["+str(day).replace("-", "")+"]]></code><value><![CDATA["+str(day).replace("-", "")+"]]></value></Row><Row uid='b582538f-204c4af6' name='기준일자(15분)' type='Metric' operator='BETWEEN' title='기준일자' useprompt='F'><code><![CDATA["+str(tmrow).replace("-", "")+"]]></code><value><![CDATA["+str(tmrow).replace("-", "")+"]]></value></Row></Filter></FilterData></AuxFilter><MeasureOption><measureformat><![CDATA[]]></measureformat><measureformatname><![CDATA[]]></measureformatname></MeasureOption><Style><item><item basestylename='Dimension' name='가로명' uid='d3a2fec6-6a36417a' rptseq='0'><Header cssname='' textalign='5'></Header><Data cssname='' textalign='5'></Data></item><item basestylename='Dimension' name='시작지점' uid='6cef7afb-926249c2' rptseq='0'><Header cssname='' textalign='5'></Header><Data cssname='' textalign='5'></Data></item><item basestylename='Dimension' name='종료지점' uid='83c0f68a-936d4207' rptseq='0'><Header cssname='' textalign='5'></Header><Data cssname='' textalign='5'></Data></item><item basestylename='Dimension' name='기준시간' uid='baa7defe-3ceb421e' rptseq='0'><Header cssname='' textalign='5'></Header><Data cssname='' textalign='5'></Data></item><item basestylename='Dimension' name='기준분' uid='cfcd1354-94414cb4' rptseq='0'><Header cssname='' textalign='5'></Header><Data cssname='' textalign='5'></Data></item><item basestylename='Measure' name='교통량(15분)' uid='f67b0e48-469a437f' rptseq='0'><Header textalign='5'></Header><Data textalign='5'></Data></item><item basestylename='Measure' name='버스 교통량(15분)' uid='e7bd8846-e941489f' rptseq='0'><Header textalign='5'></Header><Data textalign='5'></Data></item><item basestylename='Dimension' name='방면' uid='6e4ff24c-01da4c90' rptseq='0'><Header cssname='' textalign='5'></Header><Data cssname='' textalign='5'></Data></item><item basestylename='Dimension' name='순번(LV2)' uid='5e9cc154-4f984963' rptseq='0'><Header cssname='' textalign='5'></Header><Data cssname='' textalign='5'></Data></item><item basestylename='Dimension' name='구간명(LV2)' uid='4bb6cfc1-58be41cb' rptseq='0'><Header cssname='' textalign='5'></Header><Data cssname='' textalign='5'></Data></item></item></Style><SheetFormula><Formula baseuid='a3a7a0a6-91314d1c' direction='vertical' title='' fid='formula_0' showtoprow='F' groupresults='F' usecolumnformat='T'><Expression><![CDATA[AVG]]></Expression></Formula><Formula baseuid='3610af0c-1d0b46f8' direction='vertical' title='' fid='formula_1' showtoprow='F' groupresults='F' usecolumnformat='T'><Expression><![CDATA[AVG]]></Expression></Formula><Formula baseuid='290de1cc-471246fe' direction='vertical' title='합계' fid='formula_2' showtoprow='F' groupresults='F' usecolumnformat='T'><Expression><![CDATA[SUM]]></Expression></Formula><Formula baseuid='c967aa33-9f424e85' direction='vertical' title='소계' fid='formula_4' showtoprow='F' groupresults='F' usecolumnformat='T'><Expression><![CDATA[SUM]]></Expression></Formula><Formula baseuid='cfcd1354-94414cb4' direction='vertical' title='소계' fid='formula_6' showtoprow='F' groupresults='F' usecolumnformat='T'><Expression><![CDATA[SUM]]></Expression></Formula><Formula baseuid='baa7defe-3ceb421e' direction='vertical' title='합계' fid='formula_7' showtoprow='F' groupresults='F' usecolumnformat='T'><Expression><![CDATA[SUM]]></Expression></Formula><Formula baseuid='5e9cc154-4f984963' direction='vertical' title='계' fid='formula_8' showtoprow='F' groupresults='F' usecolumnformat='T'><Expression><![CDATA[SUM]]></Expression></Formula><Formula baseuid='6e4ff24c-01da4c90' direction='vertical' title='소계' fid='formula_9' showtoprow='F' groupresults='F' usecolumnformat='T'><Expression><![CDATA[SUM]]></Expression></Formula></SheetFormula><DetailView></DetailView><CellOption/><ChartOption matshowgrid='T' matshowplot='T' matusedropshadow='T' showlegend='T' bmaprow='T' xlabel='T' xaxisrot='T' charttype='cartesian' legendposition='BOTTOM_CENTER' subtype='column' tooltip='[[category]] [[value]]' zoomdirection='left' pielayout='h' ctangle='30' ctdepth='30' matminuscolor='16711931' zoomrange='10' pieinnerradius='0' pielabeldist='20' precision='0' maxchartresult='200' timeseriesduration='1000' bmapsize='10' xstagl='1' xstep='1' ytickint='0'></ChartOption><ROption s1='T' s2='T' smw='0' smh='0' pgs='2000'><script><![CDATA[]]></script><prompt><![CDATA[]]></prompt><promptvalues></promptvalues></ROption><SortOption/><WebLayout region='center' docid='dock_0' width='1338' height='362'></WebLayout><result uid=''/></Sheet><Sheet  close='F' drillreport='F' isdistinct='F' fetchall='F' fw='F' fh='T' hidetitle='F' openload='F' columnfill='T' enablepivot='T' enablecache='F' tb_vch='F' tb_prt_grd='F' tb_prt='T' showlnum='F' bcluster='F' edrill='F' name='단위 : 대' viewmode='chart' objtype='SHEET' drilltarget='sheet_0^F^^' viewchange='T' toolbutton='F' tb_prt_i='excel'><Pivot  measurelocation='column' customfix='F' usepaging='F' pagestyle='normal' dataquerymode='M_PIVOT' measuretitle='F' measureposition='0' customfixcols='0' rowperpage='20' isdistinct='F' fetchall='F' showlnum='F'><RowDimensions><item uid='d3a2fec6-6a36417a' name='가로명' itemtype='Metric' type='Metric' nodepath='/HUB/01_Data/10. 통합플랫폼/10. MART 모델, 큐브/큐브_ITS/구간 일반현황/가로명' memo='' sortorder='' activeformula='' aggrfunc='' disp_title='' hidecolumn='' timeformat=''/></RowDimensions><ColumnDimensions></ColumnDimensions><Measures><item uid='37499a1f-997a400d' name='교통량(15분)_평균' itemtype='Measure' type='Measure' nodepath='/HUB/01_Data/10. 통합플랫폼/10. MART 모델, 큐브/큐브_ITS/measures/교통량(15분)_평균' memo='' sortorder='' activeformula='' aggrfunc='' disp_title='승용차' hidecolumn='F' timeformat=''/><item uid='38a69d15-639f4d20' name='버스 교통량(15분)_평균' itemtype='Measure' type='Measure' nodepath='/HUB/01_Data/10. 통합플랫폼/10. MART 모델, 큐브/큐브_ITS/measures/버스 교통량(15분)_평균' memo='' sortorder='' activeformula='' aggrfunc='' disp_title='버스' hidecolumn='F' timeformat=''/></Measures><QueryItems></QueryItems><Clusters></Clusters><rptitems><rptitem name='단위 피봇 설계'><Filter></Filter><HavingFilter></HavingFilter></rptitem></rptitems></Pivot><UserDefinedGroup/><sql_prompts></sql_prompts><Filter></Filter><HavingFilter></HavingFilter><AuxFilter><FilterData></FilterData></AuxFilter><MeasureOption><measureformat><![CDATA[]]></measureformat><measureformatname><![CDATA[]]></measureformatname></MeasureOption><Style><item></item></Style><SheetFormula></SheetFormula><DetailView></DetailView><CellOption/><ChartOption enabledrill='T' enablezoom='T' enabledragselect='F' matshowgrid='T' matshowplot='T' matusedropshadow='T' showlegend='T' lgndfloating='F' showtitle='F' stack='F' stackperc='F' usedualaxis='T' useformula='F' swapaxis='F' bmaprow='T' bmapyaxis='F' dl_enable='F' dl_marker='F' dl_inside='F' useformatvalue='F' xlabel='T' xaxisrot='T' charttype='cartesian' legendposition='TOP_CENTER' subtype='column' title='' tooltip='[[category]] [[value]]' zoomdirection='left' relationgroups='0,1,' renderas=';;;;' dualaxisitem=';T;;;' dl_marker_l=';;;;' dl_enable_l=';;;;' maptype='us_states' yaxisformat='' yaxismin='' yaxismax='' colorset='light-color' yaxisformat2='' yaxismin2='' yaxismax2='100' pielayout='h' yaxistitle='교통량' yaxistitle2='버스 교통량' dl_align='center' tm_l_cl='F' ctangle='30' ctdepth='30' matminuscolor='16711931' zoomrange='10' rel_range1='-1' rel_range2='1' comp_range0='0' comp_range1='0' pieinnerradius='0' pielabeldist='20' precision='0' maxchartresult='200' timeseriesduration='1000' bmapsize='10' xstagl='1' xstep='1' ytickint='0' f_showvalues='F' m_zoom_level='8' m_marker='' m_min='1000' m_max='10000' s_t_f='6aa04b56-c1b0406b' s_t_fo='' e3d_en='F' e3d_al='15' e3d_be='15' e3d_de='50' e3d_vd='25'></ChartOption><ROption s1='T' s2='T' smw='0' smh='0' pgs='2000'><script><![CDATA[]]></script><prompt><![CDATA[]]></prompt><promptvalues></promptvalues></ROption><SortOption/><WebLayout region='east' docid='dock_2' width='1338' height='365'></WebLayout><result uid=''/></Sheet></Pivot><LayoutInfo type='bubble'><![CDATA[[object Object]]]></LayoutInfo><Controls><control docid='dock_1' objtype='FILTER' name='' tb_prt_i='' close='F' fw='F' fh='T' hidetitle='T' tb_prt='F'><filteroption showbutton='T' showrefresh='T' f_b_clear='T' f_t_dir='left' edrill='T'  columnsize='1' rowsize='1' brow='0' viewtype='row' buttonname='' f_b_desc='' f_b_scr='' drilltarget='sheet_0^T^^;sheet_1^T^^'></filteroption><filters><filter uid='b582538f-204c4af6' name='기준일자(15분)' nodepath='/HUB/01_Data/10. 통합플랫폼/10. MART 모델, 큐브/큐브_ITS/속도, 교통량/기준일자(15분)' type='Metric' title='기준일자' objtype='combobox' operator='BETWEEN' showperiodselector='F' objmerge='0' crowindex='0' compcss='' isnecessary='F' useprompt='F' showallvalue='T' aname='' hfilter='' showpopup='F' rangevalue='T' valueformat='' checkbuttonhor='F' invokejs='' useprevcont='F' showcondition='' defaultvalue='' yearfrom='' yearto='' startdate='' enddate='' cmap_disp='' s1a='' s1b='' s1c=''><pvalues><![CDATA[]]></pvalues><periodoption></periodoption></filter><filter uid='baa7defe-3ceb421e' name='기준시간' nodepath='/HUB/01_Data/10. 통합플랫폼/10. MART 모델, 큐브/큐브_ITS/속도, 교통량/기준시간' type='Metric' title='기준시간' objtype='combobox' operator='BETWEEN' showperiodselector='F' objmerge='0' crowindex='0' compcss='' isnecessary='F' useprompt='F' showallvalue='T' aname='' hfilter='' showpopup='F' rangevalue='T' tabid='' valueformat='' checkbuttonhor='F' invokejs='' useprevcont='F' showcondition='' defaultvalue='' yearfrom='' yearto='' startdate='' enddate='' cmap_disp='' cmap_uid='' s1a='' s1b='' s1c=''><pvalues><![CDATA[]]></pvalues><periodoption></periodoption></filter><filter uid='d3a2fec6-6a36417a' name='가로명' nodepath='/HUB/01_Data/10. 통합플랫폼/10. MART 모델, 큐브/큐브_ITS/구간 일반현황/가로명' type='Metric' title='가로명' objtype='checkbox' operator='EQ' showperiodselector='F' objmerge='0' crowindex='0' compcss='' isnecessary='F' useprompt='F' showallvalue='T' aname='' hfilter='' showpopup='T' rangevalue='F' tabid='' valueformat='' checkbuttonhor='F' invokejs='' useprevcont='F' showcondition='' defaultvalue='' yearfrom='' yearto='' startdate='' enddate='' cmap_disp='' cmap_uid='' s1a='' s1b='' s1c=''><pvalues><![CDATA[]]></pvalues><periodoption></periodoption></filter><filter uid='6e4ff24c-01da4c90' name='방면' nodepath='/HUB/01_Data/10. 통합플랫폼/10. MART 모델, 큐브/큐브_ITS/구간 일반현황/방면' type='Metric' title='방면' objtype='checkbuttons' operator='EQ' showperiodselector='F' objmerge='0' crowindex='0' compcss='' isnecessary='F' useprompt='F' showallvalue='F' aname='' hfilter='' showpopup='F' rangevalue='F' tabid='' valueformat='' checkbuttonhor='T' invokejs='' useprevcont='T' showcondition='' defaultvalue='' yearfrom='' yearto='' startdate='' enddate='' cmap_disp='' cmap_uid='' s1a='' s1b='' s1c=''><pvalues><![CDATA[]]></pvalues><periodoption></periodoption></filter></filters></control><control docid='dock_0' objtype='SHEET' fw='F' fh='F' hidetitle='F'></control><control docid='dock_2' objtype='SHEET' fw='F' fh='T' hidetitle='F'></control></Controls><ExportOption layout='portrait' pagesize='A4' fonttype='HELVETICA' filterdesc='T' pagenumber='T' showtitle='T' footer='F' repeatheader='T' scaledown='T' alldata='T' u_excel='T' u_pdf='T' u_html='T' u_csv='T' u_jasper='F' margine_top='30' margine_bottom='30' margine_left='30' margine_right='30' startpage='1' endpage='20'><jasper jasper_template='report1' pdf_output='T' html_output='T'/></ExportOption></item></smsg>",
        "uid":"84466814-713e496d",
        "option":"run",
        "active":"0",
        "pivotresult":"T",
        "jobid":str(jobid),
        "theme_id":"",
        "__i":"uid;option;active;pivotresult;jobid;theme_id",
        "_mts_":"0122483f-0155fb46",
        "uniquekey":"2017630173150",
    }
    print(jobid)
    r = requests.post("http://hubbi.its.ulsan.kr/ingecep/servlet/krcp", data=qdata, allow_redirects=True, headers=qheaders)

    # DESC : For Test Code
    # with open("a.txt", "w") as f:
    #     f.write(r.content.decode("utf-8"))

    trans = "^;@"
    patterns = regex.findall("<rw i='[0-9]*'><t>(?:<\/t><v>)?<!\[CDATA\[(.*?)\]\]>", r.content.decode("utf-8").replace(",", ""))

    with open(str(day).replace("-", "")+".csv", "w") as f:
        for p in patterns:
            f.write(p.replace(trans, ",") + "\n")

    day = tmrow
    if (day == datetime.date(2017, 7, 3)):
        break
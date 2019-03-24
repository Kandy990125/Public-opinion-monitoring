#!/usr/bin/python
# -*-coding:utf-8-*-
import json
import pandas as pd
import numpy as np
def json_get_lat_lng():
    loan_data = pd.DataFrame(pd.read_excel('data2.xlsx', header=0))
    loan_array = np.array(loan_data)
    array = []
    mydir = {'福州': [119.330221107127, 26.0471254965729],  '西安': [108.953098279196, 34.2777998978306], '沈阳': [123.432790921605, 41.8086447835158], '茂名': [110.931245330676, 21.6682257188216], '佛山': [113.134025635393, 23.0350948405144], '东城区': [116.421884701265, 39.9385740129861], '白山': [126.435797675346, 41.9458593970179], '成都': [102.899159723604, 30.3674809379575], '北京': [116.395645037879, 39.9299857780802], '重庆': [106.530635013413, 29.5446061088861], '海淀区': [116.239677801022, 40.0331620450779], '广东': [113.394817558759, 23.4080037290247], '西宁': [96.2025436722611, 35.4997610042747], '宁德': [117.984943119907, 26.0501182956607], '崇文区': [116.42463628962, 39.8892918067843], '毕节': [106.734996103304, 26.9028259277968], '深圳': [114.025973657322, 22.5460535462053], '青岛': [120.384428183682, 36.1052149012738], '南汇区': [121.76990417512, 31.0518979768205], '白银': [104.2056493285, 36.5018218287101], '上海': [121.487899485695, 31.2491617100151], '南昌': [115.893527545836, 28.6895780001412], '武汉': [114.316200102681, 30.5810841269208], '日本': [104.022612222151, 26.804452789024], '香港': [114.186124102571, 22.2935859932797], '辽宁': [122.753591557719, 41.6216001059576], '长春': [125.313642427201, 43.8983376070978], '河南': [101.556307295327, 34.5113897378692], '日照': [119.507179942994, 35.4202251931444], '其他': [104.022612222151, 26.804452789024], '山东': [118.527663392878, 36.0992899297283], '邯郸': [114.482693932342, 36.6093079284712], '连云港': [119.173872217419, 34.60154896701], '广州': [113.307649675152, 23.1200491020762], '吉林': [126.564543988833, 43.8719883343593], '洛阳': [112.447524768951, 34.6573678176511], '天津': [117.210813091553, 39.1439299033101], '杭州': [120.21937541572, 30.2592444615361], '朝阳区': [116.521694891081, 39.9589531664067], '石家庄': [114.522081844208, 38.0489583146154], '榆林': [109.745925744329, 38.2794392400706], '南通': [120.87380095093, 32.0146645408235], '宿州': [116.988692411831, 33.6367723857808], '济南': [117.02496706629, 36.6827847271614], '黄浦区': [121.496072064034, 31.2272034407689], '兰州': [103.823305440729, 36.0642255250426], '开封': [114.351642117764, 34.8018541758367], '丽水': [119.957202420664, 29.1594941207609], '福建': [117.984943119907, 26.0501182956607], '和平区': [117.202813654026, 39.1248088447028], '大庆': [128.047413714993, 47.3565916431114], '金华': [119.652575703681, 29.1028991053907], '南京': [118.778074408026, 32.0572355018059], '丹东': [124.338543114769, 40.1290228266375], '江苏': [119.368488938358, 33.0137971699539], '湖北': [112.410562192132, 31.2093162501398], '通州区': [116.740079180676, 39.8098148838513], '四川': [102.899159723604, 30.3674809379575], '湖南': [111.720663546476, 27.6958640523564], '池州': [117.494476771594, 30.6600192481606], '厦门': [118.103886045664, 24.4892306124692], '密云县': [117.001200535015, 40.532843361005], '十堰': [110.80122891676, 32.6369943394681], '丰台区': [116.258370335468, 39.8419378522047], '海口': [110.330801848336, 20.0220712769522], '韩国': [104.022612222151, 26.804452789024], '银川': [106.206478607838, 38.502621011876], '延安': [109.500509756969, 36.6033203522603], ' 河北': [117.220296765077, 39.1731489339242], '红桥区': [117.16221680792, 39.170621331225], '合肥': [117.282699091683, 31.8669422606869], '郑州': [113.649643849865, 34.7566100641402], '北碚区': [106.520342454325, 29.8665960668651], '大连': [121.593477781435, 38.9487099383043], '汕头': [116.728650288341, 23.3839084532692], '阿克苏': [81.1560131478074, 40.3494443011125], '长沙': [112.97935278765, 28.2134782308532], '新乡': [101.556307295327, 34.5113897378692], '江西': [115.676082366704, 27.7572584434408], '内蒙古': [114.415867548166, 43.468238221949], '黑龙江': [128.047413714993, 47.3565916431114], '哈尔滨': [126.657716855446, 45.7732246332393], '鞍山': [123.007763328884, 41.1187436821535], '惠州': [114.410658079971, 23.1135398524084], '贺州': [111.552594178837, 24.4110535471128], '沧州': [116.863806476442, 38.2976153503257], '吉安': [114.99203871092, 27.1138476501571], '浙江': [119.957202420664, 29.1594941207609], '张家口': [114.893781530329, 40.8111884911031], '台州': [121.591046859641, 29.142747682543], '新加坡': [104.022612222151, 26.804452789024], '苏州': [120.61990711549, 31.3179873679524], '枣庄': [117.279305383297, 34.807883078386], '莆田': [119.003571532269, 25.4255671855463], '汉中': [107.045477628725, 33.0815689781577], '太原': [112.550863589055, 37.8902770539675], '云南': [101.592951637008, 24.8642127954833], '安徽': [117.21600520757, 31.8592524170792], '墨西哥': [104.022612222151, 26.804452789024], '闵行区': [121.425024280935, 31.0935375403821], '南宁': [108.297233555866, 22.8064929356026], '静安区': [121.454755557002, 31.2353808034879], '遂宁': [102.899159723604, 30.3674809379575], '台湾': [121.973870978716, 24.0869567188049], '温州': [120.690634733709, 28.0028375940412], '嘉兴': [120.760427698957, 30.7739922395818], '黑河': [127.500830295235, 50.2506900907383], '山西': [112.515495863839, 37.8665659905093], '桂林': [110.260920147483, 25.2629012459552], '芜湖': [118.384108423228, 31.366019787543], '昌平区': [116.216456356894, 40.2217235498323], '三亚': [109.522771281359, 18.2577759148975], '定西': [104.626637600665, 35.5860562418284], '东莞': [113.763433990757, 23.0430238153682], '云浮': [112.050945958645, 22.9379756855375], '宁波': [121.579005972589, 29.8852589659181], '临沂': [118.347445071975, 35.0588777996297], '沙坪坝区': [106.374804892651, 29.6305481366288], '巴西': [104.022612222151, 26.804452789024], '昆明': [102.71460113878, 25.0491531004532], '衢州': [118.875841651508, 28.9569104475357], '西城区': [116.373190104018, 39.9342801437085], '扬州': [119.42777755117, 32.4085052545684], '常州': [119.981861013457, 31.7713967446842], '咸阳': [108.707509278196, 34.3453729959986], '株洲': [113.131695341071, 27.8274329276626], '淄博': [118.059134277869, 36.804684854212], '衡阳': [112.583818810716, 26.8981644153581], '抚州': [116.360918866931, 27.9545451702699], '江北区': [106.713614730942, 29.619317744064], '常德': [111.653718136842, 29.0121488551808], '海南': [106.925397178662, 39.2962094793918], '南开区': [117.162727949452, 39.1169872855222], '北海': [109.122627919193, 21.4727182350097], '黄石': [115.050683163924, 30.2161271277141], '镇江': [119.45583540513, 32.2044094435993], '新疆': [85.6148993383386, 42.1270009576424], '包头': [114.415867548166, 43.468238221949], '随州': [113.379358364292, 31.7178576081886], '潍坊': [119.117934235651, 36.6560051957073], '呼伦贝尔': [114.415867548166, 43.468238221949], '济宁': [116.600797624823, 35.4021216643313], '唐山': [118.183450597734, 39.6505309225366], '营口': [122.233391370793, 40.6686510664735], '贵阳': [106.709177096176, 26.6299067414409], '新余': [114.947117416789, 27.822321558629], '无锡': [120.305455900536, 31.570037451923], '周口': [114.654101942295, 33.6237408181408], '保定': [115.494810169076, 38.8865645480274], '蚌埠': [117.357079865876, 32.929498906698], '云阳县': [108.863185756751, 31.0424092672368], '贵州': [106.734996103304, 26.9028259277968], '孝感': [112.410562192132, 31.2093162501398], '浦东新区': [121.638481314092, 31.2308953491339], '商洛': [109.503789290725, 35.8600262613228], '钦州': [108.638798056423, 21.9733504653127], '湾仔区': [114.194765595006, 22.2736950393619], '绵阳': [102.899159723604, 30.3674809379575], '徐州': [117.188106623177, 34.2715534310919], '淮南': [117.018638863295, 32.6428118237479], '静海县': [116.972772261622, 38.8612621443451], '长宁区': [121.387616108665, 31.2133014968136], '牡丹江': [129.608035395637, 44.5885211527825], '三门峡': [111.181262093267, 34.7833199410497], '绍兴': [119.957202420664, 29.1594941207609], '平顶山': [113.300848977975, 33.7453014565244], '闸北区': [121.457768810215, 31.2880444659261], '江门': [113.078125341154, 22.575116783451], '杨浦区': [121.535716599635, 31.3045104795419], '内江': [105.073055991715, 29.5994615347747], '忻州': [112.72793882881, 38.4610305729589], '九龙城区': [114.203018454112, 22.3200981764961], '黔南': [107.523205110058, 26.2645359974422], '许昌': [113.835312459789, 34.0267395886552], '泰州': [119.919606016191, 32.4760532748303], '九龙坡区': [106.370594884395, 29.4345661549582], '宿迁': [119.368488938358, 33.0137971699539], '佳木斯': [130.284734585955, 46.8137796047403], '晋城': [112.867332757507, 35.4998344672256], '达州': [107.494973446589, 31.2141988589447], '徐汇区': [121.446235004729, 31.1691520895922], '阳泉': [113.569237601633, 37.8695294932226], '六盘水': [104.852086760069, 26.5918660603187], '本溪': [123.778062369792, 41.3258376266488], '宝鸡': [107.170645452383, 34.3640808097478], '呼和浩特': [111.660350520054, 40.8283188730816], '廊坊': [116.70360222264, 39.5186106250846], '承德': [117.933822455838, 40.9925210524571], '阜阳': [115.820932259046, 32.9012113305696], '加拿大': [104.022612222151, 26.804452789024], '陕西': [109.503789290725, 35.8600262613228], '松江区': [121.226790501421, 31.0212446280986], '淮安': [119.313295132638, 33.5283489669418], '湖州': [120.137243163282, 30.8779251556909], '金山区': [121.248408179751, 30.8350807770823], '澳门': [113.557519101825, 22.2041179884433], '濮阳': [115.026627440672, 35.7532978882076], '六安': [116.505252682984, 31.7555583551984], '遵义': [102.771442408042, 25.0059025488969], '中山': [113.422060020798, 22.545177514513], '中西区': [114.148788942066, 22.2854448327224], '泉州': [118.600362343229, 24.9016523839911], '九江': [115.999848021554, 29.7196395261224], '滨海新区': [117.646286270575, 39.0591766380348], '怒江': [98.8599320424821, 25.8606769781654], '德国': [104.022612222151, 26.804452789024], '巴彦淖尔市': [107.42380671968, 40.7691799024291], '卢森堡': [104.022612222151, 26.804452789024], '滨州': [117.968292414528, 37.4053139418259], '信阳': [114.08549099347, 32.1285823075117], '文山': [104.030939812463, 23.4160095350723], '乌鲁木齐': [87.5649877411158, 43.8403803472177], '清远': [113.040773348908, 23.6984685504222], '焦作': [113.211835884992, 35.2346075549859], '安庆': [117.058738772107, 30.5378978173811], '南岸区': [106.667178499036, 29.5415146189025], '齐齐哈尔': [128.047413714993, 47.3565916431114], '澳大利亚': [104.022612222151, 26.804452789024], '法国': [104.022612222151, 26.804452789024], '宜宾': [102.899159723604, 30.3674809379575], '商丘': [115.64188568785, 34.4385886402464], '四平': [124.39138207368, 43.1755247011256], '台北市': [121.520108810796, 25.0630299356117], '虹口区': [121.491918540795, 31.2824972289866], '长治': [113.120292085725, 36.2016643857434], '津南区': [117.392909959718, 38.9697905327253], '衡水': [115.686228652909, 37.7469290458567], '渝中区': [106.546966784829, 29.555236194395], '岳阳': [113.146195519116, 29.3780070754743], '珠海': [113.56244702619, 22.2569146461257], '盐城': [119.368488938358, 33.0137971699539], '安康': [109.038044563475, 32.7043704499944], '湛江': [110.36506726285, 21.2574631037643], '河东区': [117.261693165272, 39.1266256846663], '漳州': [117.676204678946, 24.5170647798085], '广西': [108.924274427059, 23.5522546881194], '赣州': [114.935909079284, 25.8452955363468], '黄大仙区': [114.214275071723, 22.3469809477773], '韶关': [113.394817558759, 23.4080037290247], '南充': [102.899159723604, 30.3674809379575], '渝北区': [106.753798531195, 29.8162640824265], '白城': [126.564543988833, 43.8719883343593], '安阳': [114.351806507672, 36.1102667221811], '自贡': [104.783891268487, 29.3521513929607], '甘肃': [102.45762459934, 38.1032673437523], '驻马店': [114.049153547456, 32.9831581540935], '大理': [100.111732088872, 25.909942635231], '邵阳': [111.461525403554, 27.2368112449224], '河西区': [117.236165450619, 39.0844937396152], '伊犁': [85.6148993383386, 42.1270009576424], '德州': [116.328161363561, 37.460825926305], '南阳': [112.542841900512, 33.0114195691165], '舟山': [122.169872098352, 30.0360103025539], '保山': [99.1779956132782, 25.1204891961903], '渭南': [109.48393269658, 34.5023579758288], '抚顺': [123.929819767054, 41.8773038295909], '秦皇岛': [119.604367616118, 39.9454615658976], '曲靖': [103.782538888027, 25.5207581428705], '襄阳': [112.410562192132, 31.2093162501398], '烟台': [121.309555030085, 37.5365615628596], '怀化': [109.986958795854, 27.5574829011728], '恩施土家族苗族自治州': [109.491923303752, 30.2858883165556], '马鞍山': [118.515881846623, 31.68852815888], '松原': [126.564543988833, 43.8719883343593], '淮北': [116.79144742863, 33.9600233053641], '鄂尔多斯': [109.997573007519, 39.8321327549039], '葫芦岛': [120.860757644756, 40.7430298813175], '昭通': [103.725020655734, 27.3406329636355], '挪威': [104.022612222151, 26.804452789024], '塘沽区': [117.649081447178, 39.0079361426824], '古巴': [104.022612222151, 26.804452789024], '花地玛堂区': [113.559451718993, 22.2102050397893], '肇庆': [112.479653369916, 23.0786632829289], '西藏': [89.1379816840313, 31.3673154027147], '大兴区': [116.425194597379, 39.6527901183645], '荷兰': [104.022612222151, 26.804452789024], '普陀区': [121.39844294375, 31.2637429290755], '德阳': [102.899159723604, 30.3674809379575], '邢台': [114.520486812944, 37.069531196912], '泰安': [117.089414917137, 36.1880777589481], '亳州': [115.787928245118, 33.8712105653019], '顺义区': [116.728229045281, 40.1549514704413], '辽源': [109.068793740743, 34.3341745295717], '石景山区': [116.184555810367, 39.9388665446455],  '武清区': [117.034577913727, 39.457042575494], '果洛': [96.2025436722611, 35.4997610042747], '宣城': [117.21600520757, 31.8592524170792], '威海': [122.093958365806, 37.5287870812514], '宁夏': [106.155481265054, 37.3213231122954], '巴音郭楞': [83.6542622237882, 42.608612242352], '鹰潭': [117.035450186012, 28.241309597182], '张家界': [110.481620156968, 29.1248893532198], '滁州': [118.324570350977, 32.3173505953838], '宣武区': [116.369352007797, 39.8915308751235], '万州区': [108.413438636699, 30.7100541843664], '防城港': [108.924274427059, 23.5522546881194], '黔西南': [106.734996103304, 26.9028259277968], '聊城': [115.986869139291, 36.455828514728], '河源': [114.713721475875, 23.757250850469], '上饶': [117.955463877149, 28.4576225539373], '武威': [102.45762459934, 38.1032673437523], '青浦区': [121.091425242822, 31.130862397997], '玉林': [110.151676316145, 22.6439736083773], '黔东南': [106.734996103304, 26.9028259277968], '南平': [118.181882948661, 26.6436264741978], '克罗地亚': [104.022612222151, 26.804452789024], '铜陵': [117.819428728806, 30.9409296946657], '喀什': [76.0143427989434, 39.513110585312], '万盛区': [106.923720518877, 28.916488600638], '平凉': [106.688911156547, 35.5501101900167], '柳州': [109.422401810151, 24.3290533524672], '昌吉': [87.073618053225, 44.1750834478909], '鹤壁': [114.297769838025, 35.755425874224], '益阳': [112.366546645226, 28.5880877798872], '汕尾': [115.3729242894, 22.7787305001639], '嘉定区': [121.251013537556, 31.3643380554336], '新西兰': [120.306815126603, 31.5832120886809], '日喀则': [88.9560627735182, 29.2681600326548], '吕梁': [111.143156602348, 37.5273160969626], '黄山': [118.077546127263, 30.2777458951202], '青海': [96.2025436722611, 35.4997610042747], '雅安': [102.899159723604, 30.3674809379575], '房山区': [115.862836312904, 39.7267526207963], '卢湾区': [121.481237978477, 31.2133483795551], '大同': [113.29050867308, 40.1137444997052], '宜春': [114.400038671558, 27.8111298958429], '攀枝花': [102.899159723604, 30.3674809379575], '揭阳': [116.379500855382, 23.5479994669261], '涪陵区': [107.340799738027, 29.6646705405597], '荆门': [112.410562192132, 31.2093162501398], '东营': [118.612643051879, 37.4086662880412], '蓟县': [117.441159221458, 40.0096136606245], '莱芜': [117.684666912472, 36.2336541336469], '赤峰': [114.415867548166, 43.468238221949], '梧州': [111.305471950073, 23.4853946367345], '景德镇': [117.186522625273, 29.3035627684483], '黄冈': [114.906618046575, 30.4461089379011], '铜仁': [109.16855802826, 27.6749026906242], '眉山': [102.899159723604, 30.3674809379575], '永川区': [105.880357603676, 29.2964876469907], '永州': [111.614647686157, 26.4359716467592], '娄底': [111.99639635657, 27.7410733023491], '临沧': [100.092612913726, 23.887806103773], '庆阳': [107.644227086733, 35.72680075453], '郴州': [113.037704467796, 25.7822639757389], '三明': [117.642193934044, 26.2708352793622], '乐山': [114.492018702858, 38.0451973356569], '泸州': [105.443970289206, 28.8959298038601], '临汾': [111.538787596408, 36.0997454435854], '凉山': [102.259590803203, 27.8923929036657], '斯洛文尼亚': [104.022612222151, 26.804452789024], '宝坻区': [117.41142059078, 39.615544004133], '潮州': [116.630075990864, 23.6618116765165], '高雄市': [121.973870978716, 24.0869567188049], '漯河': [114.046061400229, 33.5762786884831], '马来西亚': [114.18267730433, 22.2821477573992], '菏泽': [115.463359774528, 35.2624404960747], '宝山区': [121.409041218449, 31.3986226944668], '拉萨': [89.1379816840313, 31.3673154027147], '阿里': [89.1379816840313, 31.3673154027147], '希腊': [104.022612222151, 26.804452789024], '巢湖': [117.880490417033, 31.6087325475458]};

    for item in loan_array:
        dir = {}
        try:
            city = str(item[6]).split(' ')[1]
        except:
            city = str(item[6])
        label = item[7]
        if city not in mydir.keys():
            continue
        dir["name"] = city
        dir["value"] = label*10
        array.append(dir)
    print(array)
json_get_lat_lng()
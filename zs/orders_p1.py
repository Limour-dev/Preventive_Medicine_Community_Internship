def read(_r, _p, _ex, _f):
    with open(_r + _p + _ex, 'r', encoding='utf-8') as f:
        x: str
        return [_f(x.rstrip('\r\n')) for x in f]


g_others = set()

# 懒得分类了
g0 = {
    '酮体(急)', '注射用头孢唑肟钠', 'C—反应蛋白测定(急)', '磷(P)', '百特0.9%-氯化钠注射液',
    '密闭式防针刺伤型静脉留置针(美国BD 383882 Y型 22G*1.00IN 0.9mm*25mm 末端带有1个接', '复方消炎霜-丙咪氯苯乳膏',
    '黄体生成素(LH)', '免疫固定电泳（IFE）', '丙氨酸氨基转移酶（ALT）', '头孢克洛缓释片(Ⅱ)', '无创辅助通气',
    '遥测心电监护', '视黄醇结合蛋白(RBP)', '地奈德乳膏', '(帅能)复方甘草酸苷片', '甲肝病毒抗体IgM(HAV-IgM）',
    '高密度脂蛋白胆固醇(HDL-ch）', '对乙酰氨基酚缓释片', '葡萄糖氯化钠注射液', '粪隐血试验',
    '抗核提取物抗体测定(七项)', '钾(急)', '抗环瓜氨酸肽抗体(Anti-CCP)', '糖尿病低脂盐', '淀粉样蛋白A(SAA)',
    '泮托拉唑肠溶片', '注射用盐酸万古霉素', '可溶性转铁蛋白受体(sTRF)',
    '注射用艾普拉唑钠', '丙肝病毒抗体(anti-HCV)', '塞来昔布胶囊', '免疫球蛋白IgG(IgG）',
    '门冬氨酸氨基转移酶(急)', '硝酸咪康唑散', '尿液物理化学检查', '禁食', '苯溴马隆胶囊', '肌红蛋白',
    '双鹤5%-葡萄糖注射液', '血浆凝血酶时间测定（急)', '血清铁(Fe)', '注射用还原型谷胱甘肽', '钠(Na)',
    '南岳-静注人免疫球蛋白(PH4)', '甲状腺球蛋白(TG)', '膳食自理', '氨酚羟考酮片', '压力传感器(美国ICU 42584 压力 3ml)',
    '吸入用布地奈德混悬液', '一次性使用无菌导尿包(百多安 F14 标准型)', '免疫球蛋白IgG4', '凝血酶原时间测定（PT)',
    '普食低脂', '真菌/结核菌培养(血培养-真菌瓶)_血', '一般细菌涂片(革兰染色/找细菌)_尿', '二氧化碳结合力(急)',
    '酮体（β-羟丁酸)',
    '血浆蛋白S活性测定', '糖类抗原19-9(CA199)', '甘油三酯(TG)',
    '一次性使用流量设定微调精密过滤输液器 带针(金塔 恒速 JT-WL/JM（塑料瓶塞穿刺器，无', '三碘甲状腺原氨酸(T3)',
    '注射用头孢呋辛钠', '一般物理降温(最高)', '抗中性粒细胞胞浆抗体测定(ANCA)', '无针密闭输液接头(Smartsite 2000E -)',
    '布洛芬缓释胶囊', '钾(K)', '葡萄糖酸钙注射液', '谷胺酰基转移酶(急)', '一次性使用医用雾化器(英国斯莱达 20ml 口含型)',
    '硫酸镁注射液', '普食低盐', '普食', '肌酐(急)', '活化部分凝血活酶时间测定（急)', '洛索洛芬钠贴剂',
    '自粘性软聚硅酮有边型泡沫敷料(瑞典墨尼克 595400 5片/盒 15*15cm)',
    '预冲式冲管注射器(洁瑞 不带针 10ml 30支/盒 480支/箱)', '低嘌呤低脂', '淋球菌培养_尿', '红细胞生成素(EPO)',
    '甘精胰岛素注射液', '艾普拉唑肠溶片', '静脉输液', '科伦0.9%-氯化钠注射液', '病毒中和抗体（6项)',
    '载脂蛋白A-Ⅰ（ApoA-Ⅰ)', '联苯苄唑乳膏', '心肌肌钙蛋白T（急)', '盐酸吗啡注射液', '血栓弹力图试验_血小板图(双药监测)',
    '注射用甲泼尼龙琥珀酸钠', '抗磷脂酶A2受体抗体IgG', '注射用泮托拉唑钠', '半流低脂盐', '糖类抗原72-4(CA724)',
    '钙(Ca)', '氯(急)', '一次性使用压力延长管(山东威高 普通型 25根/盒)',
    '自粘性软聚硅酮有边型泡沫敷料(瑞典墨尼克 295200 5片/盒 7.5*7.5cm)', '1β（IL-1β)',
    '酮体(KBT)', '动脉采血器(英国BD 364314 3ml 22G)', '梅毒非特异性抗体（自费)', 'B型利钠肽N端片段（急)',
    '(风湿谱或自免肝)抗线粒体M2亚型测定', '雷贝拉唑钠肠溶片', '注射用奥美拉唑钠', '淋巴细胞绝对计数',
    '肺炎支原体抗体(IgG/IgM)_血', '粪常规(急)', 'MB(急)', '乳果糖口服溶液', '软食低脂盐',
    '利格列汀二甲双胍片（II)', '留置针(苏州林华 ZFII-B 24G×0.75IN（0.7×19mm) 50支/盒)',
    '一次性使用防返流引流袋(江苏康诺 II型 1500ml II型 1500ml)', '甲状腺素(T4)', '对乙酰氨基酚片', '结核菌培养_尿',
    '血小板聚集功能测定(ADP)', 'Ⅱ级护理', '特级护理', '小而密低密度脂蛋白(sdLDL)', '血常规', '乙肝病毒表面抗体(HBsAb)',
    '葡萄糖注射液', '门冬氨酸氨基转移酶（AST)', '癌胚抗原（CEA)', '超氧化物岐化酶（SOD)检测', '静注人免疫球蛋白(PH4)',
    '复方聚乙二醇电解质散（IV)', '泮托拉唑钠肠溶片', '六项呼吸道病原体核酸检测_咽拭子', '糖尿病低脂',
    '瑞巴派特胶囊', '抗心磷脂抗体分型（ACA-IgG/M/A)', '尿素(急)', '血清总铁结合力(TiBC)', '氯化钾缓释片', '人血白蛋白',
    '桉柠蒎肠溶胶囊', 'T淋巴细胞百分比(CD3)', '碱性磷酸酶(急)', '司美格鲁肽注射液', '咪达唑仑注射液',
    '叶酸片', '真菌培养_尿', '血培养_部位B(需氧瓶)_血', '一般物理降温', '糖尿病', '肌酐(Cr)', '复方甲氧那明胶囊',
    '（风湿谱)抗核小体抗体测定(AnuA)', '活化部分凝血活酶时间测定（APTT)', '脂肪酶(LIP)', '乙肝病毒核心抗体(HBcAb)',
    '普食低脂盐', 'W/O型-尿素乳膏', 'α肿瘤坏死因子（αTNF)', '常规心电图检查', '乳酸脱氢酶(LDH)', '双鹤0.9%-氯化钠注射液',
    '达格列净片', '一般细菌_痰', '直接胆红素(急)', '注射用丁二磺酸腺苷蛋氨酸',
    '一次性使用输液器(洁瑞 精密过滤(不含塑化) 15根/包 300根/箱)', '白蛋白(急)', '多烯磷脂酰胆碱注射液', '二聚体',
    '乳酸(急)', '医用外固定支具(红日 前臂 前臂)', '人胰岛素注射液', '白蛋白(ALB)', '甲氨蝶呤片',
    '一次性使用医用雾化器(英国斯莱达 成人 面罩式 成人 面罩式)', '淀粉酶(急)', '低嘌呤低脂盐', '左氧氟沙星氯化钠注射液',
    '肌红蛋白(急)', '淀粉酶(AMY)', '葡萄糖(急)', '结核菌涂片(找抗酸杆菌)_尿', '电脑多导联心电图',
    '★葡萄糖测定(干化学法简易血糖测定仪)', 'XPERT快速甲乙流/合胞病毒核酸检测', '灭菌注射用水', '总胆固醇(Tch)',
    '粪常规', '血栓弹力图试验_普通杯', '抗平滑肌抗体(ASMA)', '洛索洛芬钠片', '尿相差显微镜(门诊B7楼32号)',
    '开塞露（含甘油)', '白介素6(IL-6)', '水胶体敷料(丹麦康惠尔 3533 10*10cm)', '布美他尼注射液',
    'C肽(空腹)', '总胆红素(TB)', '内毒素鲎试验_血', '肌酸激酶同工酶(CK-MB)质量(急)', '戊肝病毒抗体IgM(HEV-IgM)',
    '乙肝病毒表面抗原(HBsAg)', '无针输液接头(贝朗 409100CN 50只/盒 腔内体积0.09ml)',
    '叶酸(FOL)', '半流低脂', '超敏促甲状腺素(s-TSH)', 'HIV抗体(anti-HIV)', '糠酸莫米松乳膏',
    '游离三碘甲状腺原氨酸(fT3)', '聚苯乙烯磺酸钠散', '降钙素原(急)', '载脂蛋白B (ApoB)',
    '总补体(CH50)', '皮质醇', '"G试验(真菌1', '动脉加压注射',
    '促甲状腺激素受体抗体(TRAb)', '半流糖尿病低脂盐', '柯萨奇B病毒IgM、IgG', '天瑞0.9%-氯化钠注射液', '补体C3(C3)',
    '双氯芬酸钠双释放肠溶胶囊', '甲胎蛋白（AFP)', '心肌肌钙蛋白T',
    '一次性无菌旋塞(艾贝尔 三通旋塞（国产材料) 三通旋塞（国产材料))', '促肾上腺皮质激素', '总胆汁酸(TBA)',
    '肌酸激酶同工酶(CK-MB)', '重组人血小板生成素注射液', '脂蛋白(a)(Lp(a))', '总蛋白(急)', '血纤维蛋白降解产物(FDP)',
    '输液器(山东新华 JMQ(PZG1) 加长 精密过滤(带针)PVC)', 'CK(急)', '皮下注射', '雷贝拉唑钠肠溶胶囊',
    '（风湿谱)抗组蛋白抗体(AHA)测定', '莫匹罗星软膏', 'I型糖尿病自身抗体谱', '琥珀酸亚铁缓释片', '乙肝病毒e抗体(HBeAb)',
    '动静脉置管护理', '多烯磷脂酰胆碱胶囊', '一般专项护理(会阴冲洗)', '免疫固定电泳（IFE)',
    '盐酸坦索罗辛缓释胶囊', '聚乙二醇洛塞那肽注射液', '阿卡波糖片', '吸入用乙酰半胱氨酸溶液', '血氨(急)',
    '注射用美罗培南', '德谷门冬双胰岛素注射液',
    '尿酸(急)', '糖蛋白1抗体', '乙肝病毒DNA（HBV-DNA)', '血浆抗凝血酶III活性测定', '秋水仙碱片', '阿利西尤单抗注射液',
    '双氯芬酸二乙胺乳胶剂', '脂蛋白相关磷脂酶A2（Lp-PLA2)', '预充式导管冲洗器(施美宁 10ml 400支/箱，50支/盒)', 'Ⅰ级护理',
    '一次性使用注射笔用针头(碧迪优泽 超薄壁 五切面 0.23*4mm（32G*4mm)超薄壁 五切面)', '度拉糖肽注射液', '心电监测',
    '\xa0', '血培养_部位B(厌氧瓶)_血', '碱性磷酸酶(ALP)', '预充式导管冲洗器(美国BD 10ML 480支/箱，30支/盒)',
    '辅酶Q10注射液', '高密度脂蛋白胆固醇(HDL-ch)', '游离甲状腺素(fT4)', '甲肝病毒抗体IgM(HAV-IgM)',
    'HIV抗体(anti-HIV)（急)', '丙氨酸氨基转移酶（ALT)', '一次性使用输液接头(爱贝尔 100只/盒 100只/盒)', '转铁蛋白(TRF)',
    '血气(监护室血气+BD针-73元)', '胰岛素(空腹)', '血培养_部位A(需氧瓶)_血', '钠Na(急)',
    '盐酸西替利嗪片', '血清蛋白电泳', '玻璃酸钠滴眼液', '蒙脱石散', '（风湿谱)抗增殖细胞核抗原抗体(抗PCNA)',
    '游离前列腺特异性抗原(f-PSA)', '半流糖尿病', '二羟丙茶碱注射液', '镁(Mg)', '血浆纤维蛋白原含量测定（急)',
    '静注人免疫球蛋白（PH4)', '肾衰宁片', '盐酸吡格列酮片', '二氧化碳结合力(CO2-CP)', '氯化钾颗粒', '谷胱甘肽片',
    '尿蛋白定量(24小时)', '碳酸氢钠注射液', '神经元特异烯醇化酶(NSE)', '免疫球蛋白IgG(IgG)', '维生素B6注射液',
    '氨酚伪麻美芬片(日片)/氨麻美敏片Ⅱ(夜片)', '总胆红素(急)', '载脂蛋白E(ApoE)',
    '留置针(日本泰尔茂 22G B型 三通带无针输液接头)', '梅毒螺旋体抗体血清试验', '鳞癌相关抗原（SCC)', '反应蛋白(hs-CRP)',
    '（风湿谱)抗核糖体抗体测定', '类风湿因子(RF)', '直接胆红素(DB)', '乙肝病毒核心抗体IgM(HBc-IgM)',
    '谷胱甘肽还原酶（GR)检测', '复方甘草酸苷片', '氯(Cl)', '总蛋白Tp', '血常规(急)', '非奈利酮片', '沙格列汀片',
    '注射用七叶皂苷钠', '乳酸脱氢酶(急)', '抗肾小球基底膜抗体测定', '18AA-II-复方氨基酸注射液', '半流', '左氧氟沙星片',
    '托伐普坦片', '一次性使用无菌导尿包(百多安 F16 标准型)', '盐酸二甲双胍片', '导尿',
    '密闭式防针刺伤型静脉留置针(美国BD 383862 Y型 24G *0.75 IN 0.7mm*19mm 末端带有1个', '炉甘石洗剂',
    '依洛尤单抗注射液', '血浆凝血酶时间测定（TT)', '谷胺酰基转移酶(γ-GT)', '双链DNA抗体定量(ds-DNA)', '复方甘草口服溶液',
    '重酒石酸去甲肾上腺素注射液', '（风湿谱)抗核提取物抗体测定(七项)', '血清胃泌素释放肽前体（ProGRP)',
    '凝血酶原时间测定(急)', '血浆纤维蛋白原含量测定（FIB)', '糖化白蛋白(GA)', '百令胶囊', '阿卡波糖胶囊', '铁蛋白(FER)',
    '褪黑素质谱法', '氯化钾注射液', '尿糖（24小时尿)', '尿酸(UA)', '大冢0.9%-氯化钠注射液'
}
g1 = {
    '糖类抗原125(CA125)', '促甲状腺激素受体刺激性抗体(TSI)', 'HIV抗体(anti-HIV)（急）', '肌酸激酶同工酶(CK-MB)质量',
    '糖基化血红蛋白(HPLC)', 'B型利钠肽N端片段', '血清胱抑素(Cystatin C)测定', 'γ-谷胺酰基转移酶(γ-GT)',
    '低密度脂蛋白胆固醇(LDL-ch)', '新型冠状病毒核酸检测', '输液器(洁瑞 300副/箱 15副/包 进气式)', '尿糖（24小时尿）',
    '抗增殖细胞核抗原抗体(抗PCNA)', '梅毒螺旋体抗体血清试验(急)',
    '留置针(日本泰尔茂 24G B型 三通带无针输液接头)', '抗""O""(ASO)',
    '狼疮抗凝物(LA)检测', '(不可单开)(风湿谱或自免肝)抗线粒体M2亚型测定', '血浆蛋白C活性测定', '乙肝病毒e抗原(HBeAg)',
    '抗核小体抗体定量', '抗核抗体(ANA)',
    '尿常规(急)', '肌酸激酶CK', '镁(急)', '酮体（β-羟丁酸）', '前白蛋白(PA)', '磷(急)', '超敏C-反应蛋白(hs-CRP)',
    '葡萄糖(空腹)', '隐血试验(急)', '戊肝病毒抗体IgG(HEV-IgG)', '降钙素原', 'α肿瘤坏死因子（αTNF）',
    '钙(急)', '一般细菌培养_尿', '抗甲状腺球蛋白抗体(anti-TG)', '尿素(BU)', '梅毒非特异性抗体（自费）',
    '前列腺特异性抗原(PSA)', '丙型肝炎病毒核心抗原', '乙肝病毒前S1抗原', '丙氨酸氨基转移酶(急)',
    '血气(心导管室/ccu-127元)', '抗心磷脂抗体分型（ACA-IgG/M/A）', '尿液有形成份检查', '抗甲状腺过氧化物酶抗体(Anti-TPO)',
    '真菌涂片(找真菌)_尿', '曲霉半乳甘露聚糖检测', '细胞角蛋白19片段(CYFRA211)',
}
g2 = {
    '氨茶碱注射液', '注射用谷胱甘肽', '抗线粒体抗体(AMA)', '非布司他片', '注射用头孢美唑钠',
    '非那雄胺片', '注射用谷胱甘肽', '0.9%-氯化钠注射液', '氧气吸入',
    '头孢克肟片', '注射用头孢曲松钠', '宽胸气雾剂', '聚卡波非钙片', '盐酸氨溴索注射液',
    '维生素B12(VitB12)', '长征0.9%-氯化钠注射液', '维生素C注射液', '奥美拉唑肠溶胶囊', '糖尿病低盐', '阿普唑仑片',
    '海康-静注人免疫球蛋白(PH4)', '静脉注射', '齐都0.9%-氯化钠注射液', '心肌肌钙蛋白T（急）', '二聚体(急)',
    '注射用盐酸瑞芬太尼', '一次性使用注射笔用针头(美国BD 329490 31G*5mm 14支/小盒 140支/大盒)',
    '左甲状腺素钠片', '艾司唑仑片', '环磷腺苷葡胺注射液', '碳酸氢钠片', '糖尿病软食低脂盐',
    '瑞巴派特片', '盐酸度洛西汀肠溶胶囊', '环磷腺苷注射液', '酒石酸唑吡坦片',
}
g3 = {
    '地高辛片', '盐酸多巴胺注射液', '去乙酰毛花苷注射液', '盐酸乌拉地尔注射液', '麝香保心丸', '临时起搏器应用',
    '冻干重组人脑利钠肽', '沙库巴曲缬沙坦钠片',  # 有利尿作用，但先不放了
}
g4 = {
    '吡格列酮二甲双胍片', '德谷胰岛素注射液', '格列美脲片', '艾托格列净片',
    '盐酸二甲双胍缓释片', '格列吡嗪控释片', '精蛋白生物合成人胰岛素注射液',
    '伏格列波糖分散片', '格列齐特缓释片',
}

g_at = {
    '贝米肝素钠注射液', '替格瑞洛片', '利伐沙班片', '磺达肝癸钠注射液', '肝素钠注射液',
    '吲哚布芬片', '硫酸氢氯吡格雷片', '甲苯磺酸艾多沙班片', '阿司匹林肠溶片', '低分子量肝素钙注射液',
    '阿司匹林肠溶缓释片', '盐酸替罗非班注射用浓溶液', '那屈肝素钙注射液', '盐酸替罗非班氯化钠注射液'
}
g_bb = {
    '琥珀酸美托洛尔缓释片', '盐酸艾司洛尔注射液', '酒石酸美托洛尔片', '盐酸阿罗洛尔片', '盐酸伊伐布雷定片',
    '富马酸比索洛尔片'
}
g_ac = {
    '盐酸贝那普利片', '培哚普利叔丁胺片', '培哚普利氨氯地平片（Ⅲ)', '培哚普利片',
}
g_ar = {
    '缬沙坦胶囊', '氯沙坦钾片', '厄贝沙坦片', '奥美沙坦酯片', '沙库巴曲缬沙坦钠片',
    '奥美沙坦酯氨氯地平片', '氯沙坦钾氢氯噻嗪片',
}
g_cc = {
    '苯磺酸左旋氨氯地平片', '硝苯地平控释片', '注射用硝普钠', '苯磺酸氨氯地平片', '培哚普利氨氯地平片（Ⅲ)',
    '奥美沙坦酯氨氯地平片', '非洛地平缓释片',
}
g_di = {
    '螺内酯片', '托拉塞米注射液', '托拉塞米胶囊', '呋塞米注射液', '注射用呋塞米',
    '注射用托拉塞米', '托拉塞米片', '呋塞米片', '氯沙坦钾氢氯噻嗪片',
}
g_st = {
    '血脂康胶囊', '瑞舒伐他汀钙片', '依折麦布片', '阿托伐他汀钙片', '非诺贝特胶囊',
}
g_am = {
    '盐酸胺碘酮注射液', '心脏电除颤术', '烟酰胺注射液', '盐酸利多卡因注射液', '盐酸胺碘酮片',
}
g_ni = {
    '硝酸甘油注射液', '单硝酸异山梨酯缓释片', '硝酸甘油片', '尼可地尔片', '硝酸甘油气雾剂',
    '单硝酸异山梨酯缓释胶囊(Ⅳ)', '硝酸异山梨酯注射液', '硝酸异山梨酯片', '单硝酸异山梨酯缓释胶囊',
}

g_99 = g_at | g_bb | g_ac | g_ar | g_cc | g_di | g_st | g_am | g_ni

all_p = read('./data/', 'time', '.txt', lambda x: x.split('\t')[0])

res = []
for p in all_p:
    one_p = read('./orders/', p, '.txt', lambda x: x.split(',')[5])
    one_at, one_bb, one_ac, one_ar, one_cc, one_di, one_st, one_am, one_ni = [0] * 9
    for item in one_p:
        item: str = item.replace('）', ')')
        if item.startswith('(') and ')' in item:
            item = item.split(')', maxsplit=1)[1]
        if 0 < item.find('-') < 4:
            item = item.split('-', maxsplit=1)[1]
        if item in g_at:
            one_at = 1
        if item in g_bb:
            one_bb = 1
        if item in g_ac:
            one_ac = 1
        if item in g_ar:
            one_ar = 1
        if item in g_cc:
            one_cc = 1
        if item in g_di:
            one_di = 1
        if item in g_st:
            one_st = 1
        if item in g_am:
            one_am = 1
        if item in g_ni:
            one_ni = 1
        if item in g_99:
            continue
        if item == '名称':
            continue
        elif item in g0:
            continue
        elif item in g1:
            continue
        elif item in g2:
            continue
        elif item in g3:
            continue
        elif item in g4:
            continue
        else:
            g_others.add(item)
    res.append('\t'.join(map(str, (
        p, one_at, one_bb, one_ac, one_ar, one_cc, one_di, one_st, one_am, one_ni),
                             )))

res = '\n'.join(res)
print(g_others)

label start:
    $ renpy.force_autosave()

    scene bg c1_01_lbp_return_v2
    with trans_opening

    narrator "李宝瓶快步穿过深夜庭院，停在崔东山房门前，抬手敲了敲门。"

    $ set_dialogue_pair("李宝瓶", "崔东山")

    voice voice_id("voice.scn_0001_midnight_courtyard_return.lbp.0001")
    a "三天后小师叔就要离开山崖书院了。李槐、裴钱他们最近经常偷偷摸摸聚在一起，就连小师叔都时不时失踪，唉"

    voice voice_id("voice.scn_0001_midnight_courtyard_return.lbp.0002")
    a "小师叔？小师叔？人呢？难道小师叔又偷偷走了？"

    voice voice_id("voice.scn_0001_midnight_courtyard_return.lbp.0003")
    a "崔东山，小师叔呢走了多久？"

    scene bg c1_01_cds_open_v1
    with trans_short

    voice voice_id("voice.scn_0001_midnight_courtyard_return.lbp.0004")
    cds "早走了啊。昨晚半夜的事情，你不知道吗？"

    voice voice_id("voice.scn_0001_midnight_courtyard_return.lbp.0005")
    a "昨晚就走了吗"

    $ story_mood_event("a", "separation")

    scene bg c1_02_midnight_lake_v1
    with trans_location

    voice voice_id("voice.scn_0002_midnight_lake.cds.0001")
    #这段音频需要分2段，
    cds "哎哎，别多想，肯定是我家先生害怕看到你现在的模样，"
    cds "上次不也这样？你小师叔明明已经换上了新衣衫新靴子，"
    cds "也一样没去书院，当时只有我陪着他，看着先生一步三回头的。"
    cds "不然我陪你去湖边散散心，聊聊我家先生？"

    voice voice_id("voice.scn_0002_midnight_lake.cds.0002")
    cds "小宝瓶，我觉得你小师叔不辞而别，太不厚道了。"
    cds "放心，只要你不认他这个小师叔，我就陪着你也不认这个先生了。你说我是不是很讲义气"

    voice voice_id("voice.scn_0002_midnight_lake.lbp.0001")
    a "你说什么呢，天底下只有不要李宝瓶的小师叔，没有不要小师叔的李宝瓶！"

    voice voice_id("voice.scn_0002_midnight_lake.cds.0003")
    cds "这样啊。"

    $ clear_dialogue_pair()

    scene bg c1_03_lh_entry_v1
    with trans_illusion

    narrator "湖水四周岸边小道上骤然间亮起一条光彩绚烂的金色光环，是以那把仙人飞剑金穗画出"
    narrator "的一座雷池，此刻崔东山撤去了其中一部分障眼法。"
    narrator "只见那李槐在远处湖边小路上，突然现身。只见这家伙手牵雪白麋鹿，学某人戴了一顶"
    narrator "斗笠，悬佩狭刀祥符，腰间晃荡着一只银白色小葫芦。李宝瓶愣了愣。"

    voice voice_id("voice.scn_0003_lihuai.lh.0001")
    c "我李槐闭关三天，终于学成了一身好武艺，这次下山闯荡江湖，要好好领教五湖四海各路豪杰的能耐。"

    scene bg c1_04_stage_far_zl_lock_test_v1
    with trans_illusion

    narrator "只见高台不远处出现了三个身影。朱敛一人扮演那剪径匪寇，一会儿拦住于禄，一会儿"
    narrator "转身逼退林守一，把两个“文弱书生”折腾得左右躲闪。"
    scene bg c1_05_lh_stop_view_high34_castfix_v2
    with None

    voice voice_id("voice.scn_0004_word_youth_elder_night.lh.0001")
    c "住手！"

    voice voice_id("voice.scn_0004_word_youth_elder_night.zl.0001")
    zl "你一样要留下过路钱，交出买命财！"

    voice voice_id("voice.scn_0004_word_youth_elder_night.lh.0002")
    c "不长眼的小小毛贼，也敢打劫我李大侠，我今天就要路见不平一声吼，你们有本事就只"
    c "管来取。哈哈哈。你没吃饭吧"

    voice voice_id("voice.scn_0004_word_youth_elder_night.zl.0002")
    zl "这这这位……少侠……好深的内力！"

    scene bg c1_05_lh_gunkai_v1
    with None

    voice voice_id("voice.scn_0004_word_youth_elder_night.lh.0003")
    c "滚开！"

    scene bg c1_05_zl_stagger_v2
    with None

    narrator "朱敛踉跄着退开几步，满脸都是遇见绝世高手的震惊。"

    voice voice_id("voice.scn_0004_word_youth_elder_night.lh.0004")
    c "实在是我武功太高，一下子没有收住手"

    voice voice_id("voice.scn_0004_word_youth_elder_night.lh.0005")
    c "记住了，我就是龙泉郡总舵、东华山分舵、学舍小舵舵主李槐！"
    c "江湖人称双拳无敌手、两脚踏山岳的‘拳脚双绝’李大侠，"
    c "我们的总舵主，便是威震天下、一统千秋的当代武林盟主——李！宝！瓶！"

    narrator "崔东山打了个响指，李槐、雪白麋鹿与朱敛，还有于禄、林守一，都消失不见。"

    scene bg c1_06_duet_lake_v1
    with trans_illusion

    voice voice_id("voice.scn_0005_du_klakeduet.narr.0001")
    narrator "接下来，只见于禄和谢谢出现在左右两侧的湖边，一人站而吹笛，一人坐而抚琴，像是"
    narrator "那江湖上的神仙侠侣。笛声幽幽，琴声悠扬，越来越激昂慷慨。"

    scene bg c1_07_pq_run_v1
    with None

    narrator "李宝瓶所在高台正对面的湖岸那边，在崔东山微微一笑后，有一个黑瘦身影刹那之间出"
    narrator "现，一路狂奔，以行山杖支撑在地，高高跃起，扑向湖中，在空中双手分别抽出腰间的"
    narrator "竹刀竹剑，身形旋转落地，有模有样，十分霸气。"
    narrator "每次裴钱落在湖面上，脚下就会出现一朵金色花朵，故而不用担心落水。"
    narrator "裴钱先以竹刀表演了一记白猿拖刀式，一鼓作气势如虎，笔直一线，奔出十数丈后，向"
    narrator "崔东山这边高台大喝一声，重重劈出一刀。"
    narrator "然后脚尖一点，踩在崔东山帮忙驾驭而出的金色花朵上，身形猛然拧转，将竹刀别回腰"
    narrator "间，落地后，以那套她自创的疯魔剑法继续向前狂奔。"
    narrator "这套独门绝学，她更是觉得天下无双；这一套剑法，裴钱打得酣畅淋漓，一气呵成。"

    scene bg c1_08_pq_pose_v1
    with None
    pause 0.35

    narrator "一个站定，收起竹剑。裴钱站在距离高台不过七八丈外的湖面上，手腕翻转，突然变出"
    narrator "那个手拈小葫芦，高高举起，仰头摆出饮酒状。"

    scene bg c1_09_platform_duet_v1
    with trans_short

    $ set_dialogue_pair("裴钱", "崔东山")

    voice voice_id("voice.scn_0006_peiqian3.pq.0001")
    peiqian "江湖没什么好的，也就酒还行。酒呢，来来来！谁来与我共饮这江湖酒"

    voice voice_id("voice.scn_0006_peiqian3.cds.0001")
    cds "我来"

    voice voice_id("voice.scn_0006_peiqian3.pq.0002")
    peiqian "好酒"

    voice voice_id("voice.scn_0006_peiqian3.cds.0002")
    cds "好酒好酒"

    voice voice_id("voice.scn_0006_peiqian3.cds.0003")
    cds "店小二，我读了些书，认了好些字，攒了一肚子学问，卖不了几文钱。"

    voice voice_id("voice.scn_0006_peiqian3.pq.0003")
    peiqian "臭豆腐好吃买不起哟"

    voice voice_id("voice.scn_0006_peiqian3.cds.0004")
    cds "山上有魑魅魍魉，湖泽江河有水鬼，吓得一转头，原来离家好多年。"

    voice voice_id("voice.scn_0006_peiqian3.pq.0004")
    peiqian "吓得我赶紧吃块臭豆腐压压惊哟"

    voice voice_id("voice.scn_0006_peiqian3.cds.0005")
    cds "哪家的小姑娘，身上带着兰花香，为何哭花了脸，你说可怜不可怜？"

    voice voice_id("voice.scn_0006_peiqian3.pq.0005")
    peiqian "吃臭豆腐哟，臭豆腐跟兰花一样香哟！"

    voice voice_id("voice.scn_0006_peiqian3.cds.0006")
    cds "试问夫子先生怎么办，树枝上挂着一只晒着日头的小纸鸢。"

    voice voice_id("voice.scn_0006_peiqian3.pq.0006")
    peiqian "爬树摘下小纸鸢，回家吃臭豆腐喽！"

    voice voice_id("voice.scn_0006_peiqian3.cds.0007")
    cds "坟前烧香神仙若少年，坟中子孙白骨已百年，你说可笑不可笑？"

    #这是崔东山在胡说八道呢，

    voice voice_id("voice.scn_0006_peiqian3.pq.0007")
    peiqian "唉？臭豆腐到底给谁吃哟？"

    voice voice_id("voice.scn_0006_peiqian3.cds.0008")
    cds "你讲你的理，我有我的拳，江湖纷纷扰扰，恩怨到底何时了？"

    voice voice_id("voice.scn_0006_peiqian3.pq.0008")
    peiqian "你再这样，我可连臭豆腐也要吃撑了哟！"

    voice voice_id("voice.scn_0006_peiqian3.cds.0009")
    cds "吃过了臭豆腐，喝过了酒，剑仙呢？"

    voice voice_id("voice.scn_0006_peiqian3.narr.0001")
    cds_peiqian "喊一声试试看？"

    $ clear_dialogue_pair()

    voice voice_id("voice.scn_0006_peiqian3.lbp.0001")
    a "小师叔！"

    scene bg c1_10_cpa_arrival_v1
    with None
    pause 0.45

    narrator "崔东山打了个响指，李槐众人都现出身形，所有人都望向东华山之巅，李宝瓶也转头望去。"
    narrator "一抹雪白身影从山顶一掠而来，气势如虹，落在了湖面之上。一身金醴法袍飘荡不已，"
    narrator "如一位白衣仙人站在了幽幽镜面。"
    narrator "陈平安并没有背负那把剑仙，只是腰间挂了一只养剑葫。陈平安一伸手，崔东山从咫尺物当中取出一把长剑"

    voice voice_id("voice.scn_0007_chengpinan.cds.0001")
    cds "走你！"

    
    scene bg c1_11_cpa_sword_01_v1
    with None
    voice voice_id("voice.scn_0008_chengpinan2.cpy.0001")
    cpa "世人皆言那积雪为粮、磨砖作镜，是痴儿，我偏要逆流而上，撞一撞那南墙！"
    cpa "饮尽江湖酒，知晓世间理，我有一剑复一剑，剑剑更快，"
    cpa "终有一天，一剑递出，便是天下头等风流快活剑……"


    scene bg c1_12_cpa_sword_02_v1
    with None
    voice voice_id("voice.scn_0008_chengpinan2.cpy.0002")
    cpa "仙人撩衣剑出袖，因势采剑画弧走。"
    cpa "定式眉眼看剑尖，剑尖之上有江山。"


    scene bg c1_12_cpa_sword_03_v1
    with None
    voice voice_id("voice.scn_0009_chengpinan3.cpy.0001")
    cpa "夜游水神庙，日访城隍阁，一叶扁舟蛟龙沟，仙人背剑如列阵……"
    cpa "世人皆说道理最无用，我却言那书中自有剑仙意，字字有剑光，"
    cpa "且教圣贤看我一剑长气冲斗牛！"

    pause 1.0

    scene bg c1_13_academy_gate_farewell_v1
    with trans_time

    narrator "一行人站在书院门口。"
    narrator "陈平安已经背好长剑剑仙和那只大竹箱。"
    narrator "裴钱斜挎包裹，手持行山杖，腰悬刀剑错。朱敛站在一旁。李槐与裴钱一番窃窃"
    narrator "私语，约好了以后一定要一起闯荡江湖"

    voice voice_id("voice.scn_0010_huyuanko.lh.0001")
    c "到了龙泉郡，一定记得帮忙看看我家宅子啊。"

    voice voice_id("voice.scn_0010_huyuanko.cpy.0001")
    cpa "没问题。你们都去学堂上课吧，不用送了，已经耽搁了不少时间，估计夫子们以后不太愿意再看到我了。"

    voice voice_id("voice.scn_0010_huyuanko.lbp.0001")
    a "小师叔，路上小心。"

    voice voice_id("voice.scn_0010_huyuanko.cpy.0002")
    cpa "小师叔还要你说。"

    voice voice_id("voice.scn_0010_huyuanko.cpy.0003")
    cpa "茅山主告辞了。"

    voice voice_id("voice.scn_0010_huyuanko.mxd.0001")
    k "以后常来"

    scene bg c1_14_autumn_road_sendoff_v2
    with trans_passage

    voice voice_id("voice.scn_0011_da_uei.cds.0001")
    cds "你们该上课的上课，该给人上课的上课，剩下的一程就由我单独送送先生，散了散了吧。"
    cds "先生，我没有觉得如今世道，变得比以前更坏了。"
    cds "山上的修道人越来越多，山下的丰衣足食，其实更多。你觉得呢？"

    voice voice_id("voice.scn_0011_da_uei.cpy.0001")
    cpa "应该是这样的。"

    voice voice_id("voice.scn_0011_da_uei.cds.0002")
    cds "但是不可否认，高出大地的山峰，像一把把剑一样，直指天幕的那些山峰，每百年千年"
    cds "之间，它们出现的次数，确实越来越少了。"
    cds "所以我希望我们所有的悲欢离合，不要都变成鸡笼外边的啄食，麻雀窝里的叽叽喳喳，枝头上的那点寒蝉凄切。"

    voice voice_id("voice.scn_0011_da_uei.cds.0003")
    cds "更高处的天空中，总要有一两声鹤唳嘶鸣，离地很远，可就是会让人感到悲伤。"
    cds "仰头见过了，听过了，就让人再难忘记。"

    voice voice_id("voice.scn_0011_da_uei.cpy.0002")
    cpa "你能这么想，我觉得很好."
    cpa "先生读书还不多，学识浅薄，暂时给不了你答案，但是我会多想想，"
    cpa "哪怕最后还是给不出答案，也会告诉你，先生想不明白，学生把先生给难住了，"
    cpa "到了那时候，学生不要笑话先生。"

    narrator "这大概是陈平安生平第一次承认，自己是崔东山的先生。"

    voice voice_id("voice.scn_0011_da_uei.cds.0004")
    cds "故乡垄头，陌上花开，先生可以缓缓归矣。"

    voice voice_id("voice.scn_0011_da_uei.cpy.0003")
    cpa "这都入秋了。"

    voice voice_id("voice.scn_0011_da_uei.cds.0005")
    cds "愿先生心境，四季如春。"

    pause 1.0
    scene black
    with trans_chapter_out
    pause 0.35

    jump chapter2_start

    return




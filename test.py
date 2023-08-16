# 实现文本数据处理，1,去除数字；2,去除多余空格；3,去除url链接；4,去除重复文本(数据集内容中重复的文本)

# testCase1
input_str = "xxxx广东省深圳市南山区桃园路50号 xxweread.qq.com/2023/8/9xx 123 广东省深圳市南山区桃园路50号https://baidu.com yyyy 阿萨德zzxc23  https://note.youda1231231o.com'https://hub.dockedasdasdar.com/,123123"


# testCase2
input_str = "xxxx广东省深圳市南山区桃园路50号 xxweread.qq.com/2023/8/9xx 123 广东省深圳市南山区桃园路50号https://baidu.com yyyy 阿萨德zzxc23  https://note.youda1231231o.com'https://hub.dockedasdasdar.com/,123123  'https://www.luyinzhushou.com/','http://192.168.1.149:8090/',asdasd a'http://github.com/dasd' 'asda  312https://doc.weixin.qq.com/水电费是的防守打法需4送达342134违法检出总数	人工确认数	违法有效数	违法无效数	无效原因																			
				未违法	号牌识别错误	没识别到号牌	号牌太模糊无法核对	残留的线（被抹去有没被完全抹去）	识别方向箭头为实线	压虚线	虚实交接处	网格线	双线一虚一实越虚线	没有从侧后方超车，而是在视线范围内变更车道	车本身没有移动	车自身移动误判为其他车移动	停车场停止车辆	识别了公交车/大巴	被动路过公交车道	辅道/不多于两道	非公交车道	在行人走后才移动	行人并没在斑马线/无过马路意图
算法检出的违法总数	本周内人工确认的违法数	人工确认的违法中采集有效，可作为违法证据处罚的数量	人工确认的违法中无法作为违法证据处罚的数量		592013	其他车型	粤01	2023/8/9 22:23:46	广东省深圳市南山区前海路辅路	违反禁止标线指示	待处理
592000	新能源大型汽车	粤B00405D	2023/8/9 21:59:57	广东省深圳市南山区深南大道9789-2	违反禁止标线指示	待处理
591997	其他车型	鲁A挂870	2023/8/9 21:49:30	广东省深圳市南山区桃园路50号	违反禁止标线指示	待处理
591987	其他车型	粤BDN58P	2023/8/9 21:34:48	广东省深圳市福田区深南新洲立交	违反禁止标线指示	待处理
591964	其他车型	粤B31396D	2023/8/9 19:37:09	广东省深圳市福田区香梅路东座	违反禁止标线指示	待处理
591956	新能源大型汽车	粤B09038D	2023/8/9 19:20:49	广东省深圳市福田区上步中路1039	违反禁止标线指示	待处理
591940	新能源大型汽车	粤B18800D	2023/8/9 18:48:07	广东省深圳市南山区深南大道9789-1	违反禁止标线指示	待处理
591938	新能源大型汽车	粤B33381D	2023/8/9 18:46:15	广东省深圳市南山区科技路2-3	违反禁止标线指示	待处理
591941	新能源大型汽车	粤B04747D	https://weread.qq.com/2023/8/9 18:36:57	广东省深圳市罗湖区沿河北路2014	违反禁止标线指示	待处理
591922	新能源大型汽车	粤B07153D	2023/8/9 18:19:21	广东省深圳市罗湖区深南东路2087号	违反禁止标线指示	待处理
591921	新能源大型汽车	粤B01708D	2023/8/9 18:10:45	广东省深圳市罗湖区深南东路5008	违反禁止标线指示	待处理
591920	其他车型	粤B8419L	2023/8/9 18:09:36	广东省深圳市福田区深南中路1019号	违反禁止标线指示	待处理
591919	新能源小型汽车	粤BDB5182	2023/8/9 18:01:42	广东省深圳市福田区深南中路3037号	违反禁止标线指示	待处理
591917	其他车型	粤B52MX7	2023/8/9 17:52:24	广东省深圳市福田区深南大道辅路	违反禁止标线指示	待处理
591915	新能源大型汽车	粤B05681D	2023/8/9 17:48:58	广东省深圳市福田区深南大道6017号	违反禁止标线指示	待处理
591895	新能源小型汽车	粤BDU3029	2023/8/9 15:46:47	广东省深圳市南山区南海大道	违反禁止标线指示	待处理
591889	新能源大型汽车	粤B41939D	2023/8/9 15:24:36	广东省深圳市罗湖区沿河北路2014	违反禁止标线指示	待处理
591866	新能源小型汽车	粤BAF2741	2023/8/9 15:02:12	广东省深圳市罗湖区深南东路5001号	违反禁止标线指示	待处理
xxxx广东省深圳市南山区桃园路50号 xxweread.qq.com/2023/8/9xx 123 广东省深圳市南山区桃园路50号https://baidu.com yyyy 阿萨德zzxc23  https://note.youda1231231o.com'https://hub.dockedasdasdar.com/,123123  'https://www.luyinzhushou.com/','http://192.168.1.149:8090/',asdasd a'http://github.com/dasd' 'asda  312https://doc.weixin.qq.com/水电费是的防守打法需4送达342134违法检出总数	人工确认数	违法有效数	违法无效数	无效原因																			
				未违法	号牌识别错误	没识别到号牌	号牌太模糊无法核对	残留的线（被抹去有没被完全抹去）	识别方向箭头为实线	压虚线	虚实交接处	网格线	双线一虚一实越虚线	没有从侧后方超车，而是在视线范围内变更车道	车本身没有移动	车自身移动误判为其他车移动	停车场停止车辆	识别了公交车/大巴	被动路过公交车道	辅道/不多于两道	非公交车道	在行人走后才移动	行人并没在斑马线/无过马路意图
算法检出的违法总数	本周内人工确认的违法数	人工确认的违法中采集有效，可作为违法证据处罚的数量	人工确认的违法中无法作为违法证据处罚的数量		592013	其他车型	粤01	2023/8/9 22:23:46	广东省深圳市南山区前海路辅路	违反禁止标线指示	待处理
592000	新能源大型汽车	粤B00405D	2023/8/9 21:59:57	广东省深圳市南山区深南大道9789-2	违反禁止标线指示	待处理
591997	其他车型	鲁A挂870	2023/8/9 21:49:30	广东省深圳市南山区桃园路50号	违反禁止标线指示	待处理
591987	其他车型	粤BDN58P	2023/8/9 21:34:48	广东省深圳市福田区深南新洲立交	违反禁止标线指示	待处理
591964	其他车型	粤B31396D	2023/8/9 19:37:09	广东省深圳市福田区香梅路东座	违反禁止标线指示	待处理
591956	新能源大型汽车	粤B09038D	2023/8/9 19:20:49	广东省深圳市福田区上步中路1039	违反禁止标线指示	待处理
591940	新能源大型汽车	粤B18800D	2023/8/9 18:48:07	广东省深圳市南山区深南大道9789-1	违反禁止标线指示	待处理
591938	新能源大型汽车	粤B33381D	2023/8/9 18:46:15	广东省深圳市南山区科技路2-3	违反禁止标线指示	待处理
591941	新能源大型汽车	粤B04747D	https://weread.qq.com/2023/8/9 18:36:57	广东省深圳市罗湖区沿河北路2014	违反禁止标线指示	待处理
591922	新能源大型汽车	粤B07153D	2023/8/9 18:19:21	广东省深圳市罗湖区深南东路2087号	违反禁止标线指示	待处理
591921	新能源大型汽车	粤B01708D	2023/8/9 18:10:45	广东省深圳市罗湖区深南东路5008	违反禁止标线指示	待处理
591920	其他车型	粤B8419L	2023/8/9 18:09:36	广东省深圳市福田区深南中路1019号	违反禁止标线指示	待处理
591919	新能源小型汽车	粤BDB5182	2023/8/9 18:01:42	广东省深圳市福田区深南中路3037号	违反禁止标线指示	待处理
591917	其他车型	粤B52MX7	2023/8/9 17:52:24	广东省深圳市福田区深南大道辅路	违反禁止标线指示	待处理
591915	新能源大型汽车	粤B05681D	2023/8/9 17:48:58	广东省深圳市福田区深南大道6017号	违反禁止标线指示	待处理
591895	新能源小型汽车	粤BDU3029	2023/8/9 15:46:47	广东省深圳市南山区南海大道	违反禁止标线指示	待处理
591889	新能源大型汽车	粤B41939D	2023/8/9 15:24:36	广东省深圳市罗湖区沿河北路2014	违反禁止标线指示	待处理
591866	新能源小型汽车	粤BAF2741	2023/8/9 15:02:12	广东省深圳市罗湖区深南东路5001号	违反禁止标线指示	待处理"

# 创建评分列表
score_list = []
total_score = 0
# range(1,11)
for i in range(1,11):
    score = float(input(f"请第{i}位评委输入评分：\n"))
    # input的输入格式
    score_list.append(score)
    # 先创建列表，再对列表进行添加
score_list.sort()
# 升序排序
print(f"去掉最低分：{score_list[0]}")
print(f"去掉最高分：{score_list[len(score_list)-1]}")
# 怎么去掉最低分的，最该分的
score_list.remove(score_list[0])
score_list.pop()

for j in score_list:
    total_score += j
print(f"选手的最终得分为：{total_score/len(score_list)}")

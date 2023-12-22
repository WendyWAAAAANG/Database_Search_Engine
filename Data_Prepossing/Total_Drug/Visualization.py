from pyecharts.charts import *
from pyecharts import options as opts

c_file = "jjum.csv"
c_data = pd.read_csv(csv_file, low_memory = False)#防止弹出警告
c_df = pd.DataFrame(csv_data)
r1 = c_df[(c_df.number>=0) & (c_df.number<100)]
r2 = c_df[(c_df.number>=100) & (c_df.number<200)]
r3 = c_df[(c_df.number>=200) & (c_df.number<300)]
r4 = c_df[(c_df.number>=300) & (c_df.number<400)]
r5 = c_df[(c_df.number>=400) & (c_df.number<500)]
number = [len(r1),len(r2),len(r3),len(r4),len(r5)]
bar = (
        Bar()
        .add_xaxis(['0-100','100-200','200-300','300-400','400-500'])
        .add_yaxis("Number",number)
        .set_global_opts(title_opts=opts.TitleOpts(title="Drug Surplus"))
    )
bar.render('DrugSurplus.html')
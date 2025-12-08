Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    latlog__single_point = Task(
        task_id = "latlog__single_point", 
        component = "Model", 
        modelName = "latlog__single_point"
    )
    raw_points = Task(
        task_id = "raw_points", 
        component = "Dataset", 
        table = {"name" : "create_point_gem_seed", "sourceType" : "Seed"}, 
        writeOptions = {"writeMode" : "overwrite"}
    )
    latlog__charts = Task(task_id = "latlog__charts", component = "Model", modelName = "latlog__charts")
    latlog__create_point = Task(
        task_id = "latlog__create_point", 
        component = "Model", 
        modelName = "latlog__create_point"
    )
    latlog__points = Task(task_id = "latlog__points", component = "Model", modelName = "latlog__points")
    latlog__distance_comparison = Task(
        task_id = "latlog__distance_comparison", 
        component = "Model", 
        modelName = "latlog__distance_comparison"
    )
    raw_points.out >> latlog__create_point.in_0
    (
        latlog__create_point.out_0
        >> [latlog__distance_comparison.in_1, latlog__points.in_0, latlog__distance_comparison.in_2,
              latlog__distance_comparison.in_0, latlog__charts.in_0]
    )
    (
        latlog__points.out_0
        >> [latlog__single_point.in_0, latlog__distance_comparison.in_0, latlog__distance_comparison.in_1,
              latlog__distance_comparison.in_2]
    )

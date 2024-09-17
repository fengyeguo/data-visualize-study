import wandb

# 登录到W&B账户
wandb.login()

# 初始化一个新的W&B项目
project_name = 'my_new_project'
run_name = 'initial_run'

# 创建新的项目（项目会在W&B UI中自动创建）
wandb.init(project=project_name, name=run_name, job_type='create_dashboard')

# 记录一些数据
for step in range(100):
    wandb.log({'x': step, 'y': step ** 2})

# 完成运行
wandb.finish()

# 使用API访问W&B
api = wandb.Api()

# 获取项目
project = api.project(project_name)

# 创建一个新的仪表板
dashboard_name = 'my_new_dashboard'
dashboard = project.create_dashboard(name=dashboard_name)

# 配置面板
panel_config = {
    'name': 'Plot Panel',
    'type': 'line',  # 面板类型为折线图
    'filters': {'metric': 'y'},  # 过滤器配置
    'configuration': {
        'x_axis': 'x',
        'y_axis': 'y',
        'title': 'Sample Plot'
    }
}

# 添加面板到仪表板
dashboard.add_panel(
    name=panel_config['name'],
    type=panel_config['type'],
    filters=panel_config['filters'],
    configuration=panel_config['configuration']
)

print(f"Dashboard '{dashboard_name}' created and panel '{panel_config['name']}' added.")

# 完成仪表板操作
wandb.finish()



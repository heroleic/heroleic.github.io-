# migrations/

此目录由 Flask-Migrate 自动生成，用于存放数据库迁移脚本。

使用步骤：
1. 初始化：`flask db init`
2. 生成迁移脚本：`flask db migrate -m '说明'`
3. 应用迁移：`flask db upgrade`
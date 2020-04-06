from test.base import BaseTest
from app.models import Admin
from app.libs.extensions import db


class CliTest(BaseTest):

    def test_admin(self) -> None:
        """测试 admin 命令"""
        result = self.runner.invoke(args=[
            'admin',
            '--username', 'newAdmin',
            '--password', '87654321',
            '--email', 'newAdmin@admin.com'
        ])
        admin = Admin.query.first()
        self.assertIn('更新管理员账户信息', result.output)
        self.assertEqual('newAdmin', admin.username)
        self.assertEqual(True, admin.check_password('87654321'))

        with db.auto_commit():
            db.session.delete(admin)
        result = self.runner.invoke(args=[
            'admin',
            '--username', 'newAdmin',
            '--password', '87654321',
            '--email', 'newAdmin@admin.com'
        ])
        self.assertIn('创建管理员账户中', result.output)

        db.drop_all()
        result = self.runner.invoke(args=[
            'admin',
            '--username', 'newAdmin',
            '--password', '87654321',
            '--email', 'newAdmin@admin.com'
        ])
        self.assertIn('请检查错误信息', result.output)

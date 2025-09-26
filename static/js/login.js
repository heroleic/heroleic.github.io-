document.querySelector('form').addEventListener('submit', function(event) {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (!username || !password) {
        alert('用户名和密码不能为空！');
        event.preventDefault();
        return;
    }

    if (password.length < 6) {
        alert('密码长度不能少于6个字符！');
        event.preventDefault();
        return;
    }
});
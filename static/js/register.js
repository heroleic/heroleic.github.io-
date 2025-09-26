document.querySelector('form').addEventListener('submit', function(event) {
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    if (!username || !email || !password || !confirmPassword) {
        alert('所有字段不能为空！');
        event.preventDefault();
        return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('请输入有效的邮箱地址！');
        event.preventDefault();
        return;
    }

    if (password.length < 6) {
        alert('密码长度不能少于6个字符！');
        event.preventDefault();
        return;
    }

    if (password !== confirmPassword) {
        alert('两次输入的密码不一致！');
        event.preventDefault();
        return;
    }
});
from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-me")

# Простая "база" заявок в памяти (для одноразового сайта достаточно)
applications = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/apply", methods=["POST"])
def apply():
    name = request.form.get("name", "").strip()
    city = request.form.get("city", "").strip()
    phone = request.form.get("phone", "").strip()
    telegram = request.form.get("telegram", "").strip()
    experience = request.form.get("experience", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not (phone or telegram):
        flash("Укажите имя и хотя бы один способ связи (телефон или Telegram).", "error")
        return redirect(url_for("index") + "#form")

    applications.append({
        "name": name,
        "city": city,
        "phone": phone,
        "telegram": telegram,
        "experience": experience,
        "message": message,
    })

    # В реальном проекте здесь можно отправлять на email / в Telegram-бот
    print("=" * 50)
    print("НОВАЯ ЗАЯВКА:")
    print(f"Имя: {name}")
    print(f"Город: {city}")
    print(f"Телефон: {phone}")
    print(f"Telegram: {telegram}")
    print(f"Опыт: {experience}")
    print(f"Сообщение: {message}")
    print("=" * 50)

    flash("Заявка отправлена. Мы свяжемся с вами в ближайшее время.", "success")
    return redirect(url_for("index") + "#form")


@app.route("/admin/applications")
def admin_applications():
    """Простой просмотр заявок (для одноразового сайта). 
    В продакшене лучше защитить паролем или убрать."""
    return render_template("admin.html", applications=applications)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

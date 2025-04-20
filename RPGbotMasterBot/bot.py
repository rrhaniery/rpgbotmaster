
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚔️ Bem-vindo ao mundo de Eltherion!

"
        "Use /criar_personagem para começar sua jornada!"
    )

async def ficha(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📜 Sua ficha será exibida aqui em breve...")

async def rolar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        expression = update.message.text.split(" ")[1]
        result = eval_dice_expression(expression)
        await update.message.reply_text(f"🎲 Rolagem: {expression} = {result}")
    except Exception as e:
        await update.message.reply_text("⚠️ Use: /rolar 1d20 ou 2d6+3")

def eval_dice_expression(expr):
    import re
    match = re.fullmatch(r"(\d*)d(\d+)([+-]\d+)?", expr)
    if not match:
        raise ValueError("Invalid format")
    count = int(match.group(1)) if match.group(1) else 1
    die = int(match.group(2))
    modifier = int(match.group(3)) if match.group(3) else 0
    return sum(random.randint(1, die) for _ in range(count)) + modifier

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ficha", ficha))
    app.add_handler(CommandHandler("rolar", rolar))
    print("Bot iniciado...")
    app.run_polling()

import instabot
bot = instabot.Bot()
bot.login(username='user', password='pass')
bot.approve_pendng_follow_requests()
bot.logout()
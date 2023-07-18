from unicaps import CaptchaSolver, CaptchaSolvingService

solver = CaptchaSolver(CaptchaSolvingService.TWOCAPTCHA, api_key="41b846c6ad3d4129b036f2f3a7d3195d")
print(solver.get_balance())
solved = solver.solve_image_captcha(open("captcha.jpeg", "rb"), is_phrase=False, is_case_sensitive=True)
print(solved.solution.text)

transcript_en_rus = {"H": ["Н", "П"], "io": "Ю", }

t = ['ибкюжпнскэмврядал']
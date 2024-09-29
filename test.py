# from elevenlabs import generate, play, save, set_api_key

# set_api_key('sk_eaf3f800db2760f5dbba2e2d901829ab4098669bd6f607cc')

# audio = generate(
#     text="Hello World",
#     voice="Bella",
#     model="eleven_multilingual_v2",
# )

# save(audio, "hello_world.wav")


from src.aigf import AIGF


AIGF().start()
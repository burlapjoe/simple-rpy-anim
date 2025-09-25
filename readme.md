# 🐎 Simple RenPy Animation Utility

This is a super simple utility for displaying an image sequence as an animation in RenPy. Doesn't reinvent anything not already in the engine, but does provide a pretty nice interface for doing so. Feel free to drop it in your own project, modify it to your needs, or whatever you like.

You can find an example below. All you need is a list of your frames in order, and then you can configure:

- Time in sec per frame `frame_time` (default 0.041666 -- eg ~24fps)
- Whether to `hold` the last frame (default True)
- Whether to `loop` (default False)
- What other images to show the animation `behind`

For longer image sequences it's recommended to cache all the frames before playing via `renpy.start_predict()`. By default, the Anim() does this automatically on init. You can have it not do so with `Anim(..., precache_on_init=False)`. From there, you can set it to automatically `precache_on_play` if you like, precache manually with `animation.precache()`, or simply skip the step entirely.


```rpy
eileen "This is a Ren'Py file"

$ sequence = ["frame0001", "frame0002", "frame0003"]

$ my_animation = ImgSeq(seq=sequence, frame_time=0.05, hold=False, behind=["eileen"], loop=True)

eileen "Watch this ball {i}bounce"

$ my_animation.play()

eileen "Remember to clean up after yourself when you don't need the animation anymore"

$ my_animation.cleanup()
```

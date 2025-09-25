init python:
    class ImgSeq:
        def __init__(self, seq, frame_time=0.041666, hold=True, behind=[], precache_on_init=True, precache_on_play=False, loop=False):
            self.seq = seq
            self.dt = frame_time
            self.hold = hold
            self.behind = behind
            self.loop = loop
            self.precache_on_play = precache_on_play
            if precache_on_init:
                self.precache()

        def play(self):
            """
            Starts playing the animation
            """
            self.hide()  # Stop any existing animation

            if self.precache_on_play:
                self.precache()
            
            displayable = self._create_animation_displayable()
            
            self.tag = "imgseq_" + str(id(self))

            renpy.show(self.tag, what=displayable, behind=self.behind)

        def _create_animation_displayable(self):
            frames = []
            for frame in self.seq:
                frames.extend([renpy.displayable(frame), self.dt])
            
            if not frames:
                return Null()

            if self.loop:
                anim = Animation(*frames)
                return Fixed(
                    Transform(anim),
                    xysize=(config.screen_width, config.screen_height)
                )
            else:
                if not self.hold:
                    frames.extend([Null(), self.dt])

                if len(frames) > 2:
                    frames[-1] = 365.25 * 86400.0  # One year
                
                anim = Animation(*frames)
                return Fixed(
                    Transform(anim),
                    xysize=(config.screen_width, config.screen_height)
                )

        def hide(self):
            """
            Removes the animation from the scene
            """
            if hasattr(self, 'tag'):
                renpy.hide(self.tag)
                del self.tag

        def precache(self):
            for img in self.seq:
                renpy.start_predict(img)
        
        def cleanup(self):
            """
            Removes the animation from the scene and all the frames from the cache
            """
            self.hide()
            for img in self.seq:
                renpy.stop_predict(img)
        
        def __del__(self):
            self.cleanup()

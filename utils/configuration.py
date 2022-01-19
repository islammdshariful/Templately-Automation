
class Config:
    display = 1
    LIVE = False
    DEV = False
    user = ""

    def set_env(self, env):
        if env.__eq__('live'):
            self.LIVE = True
        elif env.__eq__('dev'):
            self.DEV = True
        else:
            print("\nPLEASE CHOOSE A CORRECT ENVIRONMENT. EX: dev OR live")
            exit()

    def get_env_live(self):
        return self.LIVE

    def get_env_dev(self):
        return self.DEV

    def get_url(self, url):
        if self.LIVE:
            root = "https://templately.com/"
            signup = root + "signup"
            signin = root + "signin"

            if url.__eq__('root'):
                return root
            elif url.__eq__('signup'):
                return signup
            elif url.__eq__('signin'):
                return signin
            else:
                print("PLEASE CHOOSE A CORRECT URL. EX: root, signup, signin etc")
                return 0

        if self.DEV:
            root = "https://templately.dev/"
            signup = root + "signup"

            if url.__eq__('root'):
                return root
            elif url.__eq__('signup'):
                return signup
            else:
                print("PLEASE CHOOSE A CORRECT URL. EX: root, signup, signin etc")
                return 0




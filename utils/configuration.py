
class Configuration:
    display = 1
    LIVE = False
    DEV = False
    user = ""

    def __init__(self, read_credentials):
        self.credential = read_credentials

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
            cred_root = self.credential["dev"]["root"]
            root = "https://templately.dev/"
            signup = root + "signup"

            if url.__eq__('root'):
                return cred_root
            elif url.__eq__('signup'):
                return signup
            else:
                print("PLEASE CHOOSE A CORRECT URL. EX: root, signup, signin etc")
                return 0




import commands2

# It is important, for some unknown reason, to force the CommandScheduler
# singleton to be created before any phoenix libraries are imported. If you
# don't do this we get a hang at shutdcown.
_ = commands2.CommandScheduler.getInstance()

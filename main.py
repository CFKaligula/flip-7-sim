from flip_seven_sim.simulation import Simulation
from flip_seven_sim.strategy import AlwaysGiveUp, GiveUpAfterFive, GiveUpAfterFour, GiveUpAfterThree, GiveUpAfterTwo, NeverGiveUp, NoHigh, NoMid, Random


def main():
    sim = Simulation(
        strategies=[
            NoHigh(),
            Random(),
            Random(),
            Random(),
            NeverGiveUp(),
            AlwaysGiveUp(),
            GiveUpAfterFive(),
            GiveUpAfterFour(),
            GiveUpAfterThree(),
            GiveUpAfterTwo(),
            NoMid(),
        ]
    )
    sim.run(n_rounds=int(1e7))


if __name__ == '__main__':
    main()

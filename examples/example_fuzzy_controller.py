# -*- coding: utf-8 -*-
# Copyright © 2022 Thales. All Rights Reserved.
# NOTICE: This file is subject to the license agreement defined in file 'LICENSE', which is part of
# this source code package.
import skfuzzy.control

from src.kesslergame import KesslerController
from typing import Dict, Tuple
import skfuzzy.control as ctrl
import skfuzzy as skf
import numpy as np


class FuzzyController(KesslerController):
    def __init__(self):
        """
        Any variables or initialization desired for the controller can be set up here
        """
        ...

    def create_fuzzy_systems(self):
        distance = ctrl.Antecedent(np.arange(0.0, 1.0), "distance")
        angle = ctrl.Antecedent(np.arange(0.0, 1.0), "angle")

        firing_angle = ctrl.Consequent(np.arange(0, 26, 1), "firing_angle")

        distance.automf(5)
        angle.automf(5)





    def actions(self, ship_state: Dict, game_state: Dict) -> Tuple[float, float, bool, bool]:
        """
        Method processed each time step by this controller to determine what control actions to take

        Arguments:
            ship_state (dict): contains state information for your own ship
            game_state (dict): contains state information for all objects in the game

        Returns:
            float: thrust control value
            float: turn-rate control value
            bool: fire control value. Shoots if true
            bool: mine deployment control value. Lays mine if true
        """

        thrust = 50
        turn_rate = -90
        fire = True
        drop_mine = False

        return thrust, turn_rate, fire, drop_mine

    @property
    def name(self) -> str:
        """
        Simple property used for naming controllers such that it can be displayed in the graphics engine

        Returns:
            str: name of this controller
        """
        return "Test Controller"

    # @property
    # def custom_sprite_path(self) -> str:
    #     return "Neo.png"

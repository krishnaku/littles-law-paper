# -*- coding: utf-8 -*-
# Copyright: © Exathink, LLC 2016-2015-${today.year} All Rights Reserved

# Unauthorized use or copying of this file and its contents, via any medium
# is strictly prohibited. The work product in this file is proprietary and
# confidential.

# Author: Krishna Kumar

"""
Registry for delay behaviors. See module behavior for examples of registered behaviors.
"""

from sim.model import Registry
from sim.model.delay.protocol import DelayBehavior


delay_behavior_registry: Registry[DelayBehavior]= Registry()

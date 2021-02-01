'''
    This file is part of PM4Py (More Info: https://pm4py.fit.fraunhofer.de).

    PM4Py is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PM4Py is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with PM4Py.  If not, see <https://www.gnu.org/licenses/>.
'''
from pm4py.util.xes_constants import DEFAULT_NAME_KEY
from pm4py.statistics.parameters import Parameters
from pm4py.util import exec_utils


def get_start_activities(log, parameters=None):
    """
    Get the start attributes of the log along with their count

    Parameters
    ----------
    log
        Log
    parameters
        Parameters of the algorithm, including:
            Parameters.ACTIVITY_KEY -> Attribute key (must be specified if different from concept:name)

    Returns
    ----------
    start_activities
        Dictionary of start attributes associated with their count
    """
    if parameters is None:
        parameters = {}
    attribute_key = exec_utils.get_param_value(Parameters.ACTIVITY_KEY, parameters, DEFAULT_NAME_KEY)

    start_activities = {}

    for trace in log:
        if len(trace) > 0:
            if attribute_key in trace[0]:
                activity_first_event = trace[0][attribute_key]
                if activity_first_event not in start_activities:
                    start_activities[activity_first_event] = 0
                start_activities[activity_first_event] = start_activities[activity_first_event] + 1

    return start_activities
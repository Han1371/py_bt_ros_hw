from modules.base_env import BaseEnv
import os
from modules.utils import config 
from modules.base_agent import BaseAgent as Agent

# Load behavior tree
behavior_tree_xml = f"{os.path.dirname(os.path.abspath(__file__))}/{config['agent']['behavior_tree_xml']}"

class Env(BaseEnv):
    def __init__(self, config):
        super().__init__(config)

        # Initialise
        self.reset()

    def reset(self):
        super().reset()

        ros_namespace = config['agent'].get('namespaces', [])

        # Initialize agent
        self.agent = Agent(ros_namespace)

        # Provide global info and create BT
        self.agent.create_behavior_tree(behavior_tree_xml)        

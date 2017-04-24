class POMDP(object):
    def __init__(self, stuff):
        pass
    
    def prob_obs_given_bs_a(self, b_s, a):
        return 1.0
    
    def bayes_update(self, b_s, a, o):
        return b_s
    
    def cost(self, b_s, actions, observations):
        return 0.0
    
    def heuristic(self, b_s):
        return 0.0
    
    def get_possible_actions(self, b_s):
        return []
    
    def get_possible_observations(self, b_s, a):
        # N x {0,1} x {0,1} x {0,1}
        return []
    
    def solve(self, b_s_init):
        pass

    
class Node(object):
    def __init__(self, pomdp, b_s, is_obs_node, parent=None):
        self.pomdp = pomdp
        self.b_s = b_s
        self.parent = parent
        self.is_obs_node = is_obs_node
        
    def get_children(self):
        return []
    
    def get_parent(self):
        return self.parent
    

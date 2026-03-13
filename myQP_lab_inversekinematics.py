import os

import numpy as np
from numpy import linalg as la
from qpsolvers import Problem, available_solvers, solve_problem


def getTorques(W, dq_free, iE, iA, q_s, q_t, q_e, q_a):
    """

    Args:
        W: compliance matrix (size of 7 by 7)
        dq_free: free motion vector (size of 7)
        iE: indices of the effector in the system (W and dq_free)
        iA: indices of the actuators in the system (W and dq_free)
        q_s: position (x,y,z) of the sensor (real marker)
        q_t: position (x,y,z) of the target
        q_e: position (x,y,z) of the effector in the simulation (simulation marker)
        q_a: current displacement (angle in randian) of the motors (d0, d1, d2, d3)

    Returns:
        torques: corresponds to the motor torques to apply

    """
    # Build the inverse problem system using the matrices provided by SOFA.
    #
    # Minimize 1/2 x'*P*x + q'*x
    # subject to G*x <= h,
    #            A*x = b,
    #         and lb <= x <= ub

    # Note that:
    #      1. You can access a block Wii of the matrix W by doing:
    #         Wii = W[indices, :][:, indices]
    #      2. W and dfree are numpy matrices, so the you can use the @ operator
    #         for the matrices product, ex: W @ dfree
    #      3. W.T gives you the transpose of the matrix W

    Wea = W[iE, :][:, iA]
    Waa = W[iA, :][:, iA]
    # H_a @ dq_free
    Ha_dq_free = dq_free[iA]
    da_free = Ha_dq_free + q_a
    He_dq_free = dq_free[iE]
    y_e = q_t 

    P = None
    q = None
    G = None
    h = None
    A = None
    b = None

    lb = None
    ub = None

    ############# Exercise i): Fill in below ###########################
    # Implement the cost function in standard form
    P = None
    q = None

    ############################

    ############# Exercise ii): Fill in below ###########################
    # Add a constraint on the motors' displacement
    # Uncomment the following lines to add them to the optimization problem.
    
    # Question: reverse-engineer what the role of G, h, A, and b are and comment. 

    # G = np.matrix([-Waa[0, :], Waa[1, :], -Waa[2, :], Waa[3, :]])
    # h = np.array([1, 1, 1, 1]) + [da_free[0], -da_free[1], da_free[2], -da_free[3]]

    # A = np.array(Waa[[0], :])
    # b = np.array([-0.5 - da_free[0]])

    ############################

    ############# Exercise iii): Fill in below ###########################
    # Uncomment the following lines to add an energy term to the minimization.
    # This will help in the case of multiple solutions, the solver will converge to the one that
    # minimizes the work of the actuators.

    # Question: change this value (weight=1, weight=0, weight=0.01) and try to understand what is happening.

    # weight = 0.01 
    # P += weight * la.norm(P) / la.norm(Waa) * Waa

    ############################

    torques = [0.0, 0.0, 0.0, 0.0]
    if P is not None:
        try:
            ############# Exercise i): Fill in below #####################
            # Solve the problem using at least two of the available solvers. 

            # Question: do a quick read to make sure the solvers are compatible and comment. 
            torques = None
            ############################

        except Exception as e:
            import Sofa
            Sofa.msg_error(os.path.basename(__file__), str(e))
            raise e
    return torques


def test_getTorques():
    W = np.random.rand(7, 7)
    dq_free = np.random.rand(7)
    iE = [0, 1, 2]
    iA = [3, 4, 5, 6]
    q_s = np.random.rand(3)
    q_t = np.random.rand(3)
    q_e = np.random.rand(3)
    q_a = np.random.rand(4)

    return getTorques(W, dq_free, iE, iA, q_s, q_t, q_e, q_a)


if __name__ == "__main__":
    print(available_solvers)
    output = test_getTorques()
    print("output:", output)

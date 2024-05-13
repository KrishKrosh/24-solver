import streamlit as st
from card_game_solver import CardGameSolver

def main():
    st.set_page_config(page_title="24 Game Solver", page_icon="🧩")
    st.title('24 Game Solver')
    solver = CardGameSolver()

    # Collapsible configuration section
    with st.expander("Configuration", expanded=False):
        new_target = st.number_input('Set a new target value (default is 24):', value=solver.target, min_value=1, step=1)
        if new_target != solver.target:
            solver.change_target(new_target)
            st.experimental_rerun()

    st.header("Input your hand")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        num1 = st.number_input('First number:', min_value=1, max_value=13, step=1, key='num1', format='%d')
    with col2:
        num2 = st.number_input('Second number:', min_value=1, max_value=13, step=1, key='num2', format='%d')
    with col3:
        num3 = st.number_input('Third number:', min_value=1, max_value=13, step=1, key='num3', format='%d')
    with col4:
        num4 = st.number_input('Fourth number:', min_value=1, max_value=13, step=1, key='num4', format='%d')

    hand = [num1, num2, num3, num4]

    if st.button('Solve for ' + str(solver.target)):
        if all(num > 0 for num in hand):
            solutions = solver.solve(hand)
            if solutions:
                solutions_list = list(solutions)
                num_solutions = len(solutions_list)
                main_solution = solutions_list[0]
                st.success(f"{num_solutions} solution(s) found:")
                st.markdown(f"## {main_solution}")
                if len(solutions_list) > 1:
                    with st.expander("See all solutions"):
                        st.write('\n'.join(f"- {solution}" for solution in solutions_list[1:]))
            else:
                st.error("No solutions found for this hand.")
        else:
            st.error("Please input all four numbers for the hand.")

    if st.checkbox('Show all operation combinations'):
        operations = solver.generate_operation_combinations()
        st.write(operations)

if __name__ == "__main__":
    main()

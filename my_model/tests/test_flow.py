from my_model.flow import flow, output_variables


def test_flow_execution(tmp_path):
    # mark success on success of evaluate task
    flow.set_reference_tasks([output_variables])

    # Running without passing parameters require defaults for all parameters
    flow_run = flow.run(filename=f"{tmp_path}/test_file.txt", filesystem_identifier="local")

    # check success of flow
    assert flow_run.is_successful()

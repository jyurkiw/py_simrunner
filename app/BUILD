py_library(
    name='sim_runner_lib',
    srcs=[
        'sim_runner.py'
    ],
    visibility=['//visibility:public'],
    deps=[
        "//simrunner/app/lib:api_lib"
    ]
)

py_binary(
    name = "sim_runner",
    srcs = [
        "sim_runner.py"
    ],
    main = "sim_runner.py",
    deps = [
        ":sim_runner_lib"
    ]
)
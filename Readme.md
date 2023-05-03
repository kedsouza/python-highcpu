# How to profile cpu with cProfile

- Download this example using `git clone https://github.com/azureossd/python-performance-samples.git`
- Cd into **python-performance-samples/cpu/cprofile_initial/**


---

## Create a virtual environment and install dependencies
1. Create a virtual environment with any python version >=3.
    - If you are using Windows:
        ```shell
            python -m venv env
        ```
    - If you are using Linux:
        ```shell
            python3 -m venv env
       ```
2. Activate the virtual environment.
    - If you are using Windows in cmd:
        ```shell
            env\Scripts\activate
        ```
    - If you are using Linux
        ```shell
            source env/bin/activate
        ```
3. Once the virtual environment is activated, install **requirements.txt**.
    ```shell
        pip install -r requirements.txt
    ```

## Configuring cProfile
1. You need to import the following modules:
```python
    import cProfile, pstats, io
    from pstats import SortKey
```
2. Select the function/method or route that you think it is taking more CPU time. To enable/disable the profile you will need the following code

```python
    pr = cProfile.Profile()
    pr.enable()
    # ... do something ...
    result = firstMethod()

    pr.disable()

    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
```
3. Run the application with `python app.py` and get cProfile output. 
4. To avoid stdout, you can write the output to a log file with `ps.dump_stats` as followed:

```python
    pr = cProfile.Profile()
    pr.enable()
    # ... do something ...
    result = firstMethod()
    pr.disable()

    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.dump_stats('output.txt')
```

## Using cprofilev
In this case that you have generated a output file, this file will be hard to read if you open it, you will need another viewer. 

You can use this library **cprofilev**
- To install this tool:
    ```shell
        pip install cprofilev
    ```
- To run this tool you will need to pass the file as argument as followed:

    ```shell
        cprofilev -f output.txt
    ```
- The viewer will be listening in **http://127.0.0.1:4000**




## Profiling a script 

For this sample you don't need any virtual environment since there are not extra libraries to be installed.

You can run cProfile without adding any additional code as followed:

```shell
    python -m cProfile [-o output_file] [-s sort_order] name.py
```
Example:

```shell
    python3 -m cProfile -s cumtime -o output.txt script.py
```

- Where -m to define which module to run, in this case a cProfile library.
- Where -s you can order by calls, cumulative, cumtime, file, filename, module, ncalls, tottime, time, etc.
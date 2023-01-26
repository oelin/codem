# CodeM



## Introduction

CodeM is a simple code-in-markdown compiler written in Python, and configurable using YAML. Code-in-markdown is a documentation style where source code and documentation are written side-by-side in markdown (`.md`) files. This format closely resembles notebooks commonly used in scientific computing contexts. CodeM works by stripping all non-source-code sections from a markdown file, leaving only interpretable code. For instance, consider the following code-in-markdown file:

<pre>
# The `add()` function

This function adds two numbers together.

```py
def add(x, y):
  return x + y
```

Lorem ipsum...
</pre>

After compilation, CodeM will produce the following source file:

```py
def add(x, y):
  return x + y
```

## Configuration

CodeM uses YAML to specify transformation rules on source and target files. For instance, the following `codem.yaml` file instructs CodeM to convert all `md` files in `./app` to `js` files in `src`.

```yaml
# Codem Configuraton File

output: src

rules:
        - name: JavaScript Rule
          from: md
          to: js
          locations:
                  - ./app
```

A full specification of CodeM YAML directives will be added to this section shortly.

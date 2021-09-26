<p align="center">
<img src="https://res.cloudinary.com/wemakeart/image/upload/v1632678403/learn-bundler/learn-bundle_vcpcga.png" width=150px height="150px"  alt="docs-icon"/>
</p>

# Learn Bundler

---

Simple POC repository for learning playwright-python. The goal is to create an application in python that leverages playwright to screenshot and save a Microsoft Learn module. All units should be bundled and stored in a specific **export** directory, inside a sub-directory identified by the module name.

**NOTE** - Current output format mainly suits mobile devices. That was the initial goal of the project so that a user could review modules on their mobile device whilst preparing for their next exam.

## 🚧 Clear Issues 🚧

* Multiple instances being created in **pw_microsoft_learn.py** module. In future, single instance will be created and context will be passed down for a single export task. Reasoning for current implementation, modularity.
* Static implementation of CLI handler.
import cadquery as cq

step_file = "623016201.STEP"
result = cq.importers.importStep(step_file)
cq.exporters.export(result, "model.stl")


from ultralytics.nn import SegmentationModel

model = SegmentationModel(r"ultralytics\cfg\models\11\FS-ITMR.yaml",ch=13,nc=1)
print(model)
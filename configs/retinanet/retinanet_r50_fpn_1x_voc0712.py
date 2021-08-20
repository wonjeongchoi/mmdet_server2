_base_ = [
    '../_base_/models/retinanet_r50_fpn.py',
    '../_base_/datasets/voc0712.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
# model
model = dict(bbox_head=dict(num_classes=20))  # voc0712 dataset has 20 classes
# optimizer
optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001)  # lr=0.01 for 4 GPUs * 2 imgs/gpu
# learning policy
runner = dict(max_epochs=1)  # just for simple test

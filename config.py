conf = {
    "WORK_PATH": "E:\\Learn\\NCKH\\GaitSet\\work",
    "CUDA_VISIBLE_DEVICES": "0",
    "data": {
        'dataset_path': "E:\\Learn\\NCKH\\GaitSet\\output",
        'resolution': '64',
        'dataset': 'CASIA-B',
        # In CASIA-B, data of subject #5 is incomplete.
        # Thus, we ignore it in training.
        # For more detail, please refer to
        # function: utils.data_loader.load_data
        'pid_num': 73,
        'pid_shuffle': False,
    },
    "model": {
        'hidden_dim': 256,
        'lr': 1e-4,
        'hard_or_full_trip': 'full',
        'batch_size': (8, 16),
        'restore_iter': 0,
        'total_iter': 80000,
        'margin': 0.2,
        'num_workers': 4,
        'frame_num': 30,
        'model_name': 'GaitSet',
    },
}

TrungHC
Phát triển ứng dụng nhận diện và điểm danh sinh viên trong các lớp học tại trường Đại học Thủy lợi.

github: https://github.com/hct97/face_attandace

-->
#install lib
pip3 install -r requirements.txt

#process images
python3 src/align_dataset_mtcnn.py Dataset/FaceData/raw Dataset/FaceData/processed --image_size 160 --margin 32 --random_order --gpu_memory_fraction 0.25

#train model
python3 src/classifier.py TRAIN Dataset/FaceData/processed Models/20180402-114759.pb Models/facemodel.pkl --batch_size 1000

#open camera
python3 src/face_rec_cam.py

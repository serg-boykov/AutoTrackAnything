import subprocess
import settings


def run_tracking(video_path, width, height, frames_to_propagate, output_video_path, device, person_conf, kpts_conf,
                 iou_thresh, yolo_every, output_path):
    # Формируем список аргументов для передачи в команду
    args = [
        'python',  # Команда для запуска Python
        'tracking.py',  # Имя файла, который нужно запустить
        '--video_path', video_path,
        '--width', str(width),
        '--height', str(height),
        '--frames_to_propagate', str(frames_to_propagate),
        '--output_video_path', output_video_path,
        '--device', str(device),
        '--person_conf', str(person_conf),
        '--kpts_conf', str(kpts_conf),
        '--iou_thresh', str(iou_thresh),
        '--yolo_every', str(yolo_every),
        '--output_path', output_path
    ]

    # Запускаем файл tracking.py с указанными аргументами
    subprocess.run(args)


if __name__ == '__main__':
    # Здесь вы можете указать заранее заданные параметры
    video_path = 'video_fragment_178.31.03.2023_original.mp4'
    width = 1280
    height = 768
    frames_to_propagate = 600
    output_video_path = 'RESULT_VIDEO_PATH.mp4'
    device = 0
    person_conf = 0.6
    kpts_conf = 0.4
    iou_thresh = 0.15
    yolo_every = 2
    output_path = 'OUTPUT_CSV_PATH.csv'

    # Вызываем функцию, которая запускает tracking.py с указанными параметрами
    run_tracking(video_path, width, height, frames_to_propagate, output_video_path, device, person_conf, kpts_conf,
                 iou_thresh, yolo_every, output_path)

import csv

import csv_my

with open('test.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter='$')
    writer.writerow(['user_id', 'user-name', 'comments_qty'])
    writer.writerow([5235, 'Artuom', 1352])
    writer.writerow([4428, 'Mike', 246])
    writer.writerow([1684, 'Alice', 73])

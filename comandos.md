### Lanzar docker
```bash
docker run --hostname=quickstart.cloudera --privileged=true -t -i --cpus=12 -v /home/juanjo/repos/muei/ics/ejercicio1:/home/cloudera/ejercicio1 --publish-all=true -p 7180 cloudera/quickstart /usr/bin/docker-quickstart
```

### Lanzar HDFS (dentro de docker)
```bash
hdfs dfs -put sources
```

### Hacer un ls en el HDFS
```bash
hdfs dfs -ls sources 
```

### Lanzar código en Hadoop
```bash
/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar -D mapreduce.job.reduces=2 -input sources -output output_dir -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py
```

### Hacer un rm del directorio en el HDFS
```bash
hdfs dfs -rmdir sources 
```
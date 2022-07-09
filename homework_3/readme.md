## Для запуска redis нужно создать и запустить контейнер командой

docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest

## Команды redis-cli:

- keys * - все ключи
- get key - получить значение по ключу
- flushall - очистить базу redis
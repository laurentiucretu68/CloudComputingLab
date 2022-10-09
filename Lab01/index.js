require('dotenv').config()
const fastify = require('fastify')({ logger: false })
const multipart = require('@fastify/multipart')
const formBody = require('@fastify/formbody')
const view = require("@fastify/view")

const start = async () => {
    try {
        await fastify.register(multipart)
        await fastify.register(formBody)
        await fastify.register(view, {
            engine: {
                ejs: require("ejs"),
            },
        });
        await fastify.register(require('./routes/index'))

        await fastify.listen({
            port: process.env.PORT,
            host: process.env.HOST
        })
    } catch (error){
        console.log(error)
        process.exit(1)
    }
}
start().then(r => r)
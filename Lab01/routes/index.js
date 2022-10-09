'use strict'

const fs = require('fs')
const Path = require('path')
const axios = require('axios')

async function router(fastify){
    fastify.get('/home', async (req, res) => {
        let imagesJson = []
        if (fs.readFileSync(Path.resolve(__dirname, '../images', "index.json")).toString() !== '')
            imagesJson = JSON.parse(fs.readFileSync(Path.resolve(__dirname, '../images', "index.json"), "utf-8"))

        res.view("/templates/index.ejs", {
            imagesJson: imagesJson
        })
        return res
    })

    fastify.post('/download', async (req, res) => {
        try {
            const { imageLink, imageName } = req.body

            const url = imageLink
            const path = Path.resolve(__dirname, '../images', imageName)
            const writer = fs.createWriteStream(path)

            const response = await axios({
                url: url,
                method: "GET",
                responseType: 'stream'
            })

            await response.data.pipe(writer)

            /// Save to JSON file
            let imagesJson = []
            if (fs.readFileSync(Path.resolve(__dirname, '../images', "index.json")).toString() !== '')
                imagesJson = JSON.parse(fs.readFileSync(Path.resolve(__dirname, '../images', "index.json"), "utf-8"))
            const currentImage = {
                imageName,
                imageLink,
                localLink: path.toString()
            }
            let duplicate = false
            imagesJson.forEach(image => {
                if (image.imageName === currentImage.imageName){
                    duplicate = true
                }
            })
            if (!duplicate){
                imagesJson.push(currentImage)
            }
            fs.writeFileSync(Path.resolve(__dirname, '../images', "index.json"), JSON.stringify(imagesJson), "utf-8")

            res.redirect('/home?success=true')

        } catch (error){
            console.error(error)
            res.redirect(`/home?success=false`)
        }
        return res
    })

    fastify.get('*', async (req, res) => {
        res.view("/templates/notFound.ejs")
        return res
    })
}

module.exports = router
import aiohttp
import iaofiles
from Vars import Var
from aiohttp import ContentTypeError
from plugins.Helper.check_filename import check_filename

async def RemoveBG(input_file_name):
    RMBG_API = Var.RMBG_API
    headers = {"X-API-Key": RMBG_API}
    files = {"image_file": open(input_file_name, "rb").read()}
    async with aiohttp.ClientSession() as ses:
        async with ses.post(
            "https://api.remove.bg/v1.0/removebg", headers=headers, data=files
        ) as out:
            contentType = out.headers.get("content-type")
            if "image" not in contentType:
                return False, (await out.json())

            name = check_filename("hagadmansa-rmbg.png")
            file = await aiofiles.open(name, "wb")
            await file.write(await out.read())
            await file.close()
            return True, name

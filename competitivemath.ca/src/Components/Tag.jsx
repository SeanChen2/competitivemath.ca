

export default function Tag({ children }) {
    console.log(children)

    return (
        <li className="bg-blue-200 p-1 text-xs">
            {children}
        </li>
    )
}